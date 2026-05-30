// TopicFlow - Main JavaScript File
// Frontend logic for the TopicFlow AI Educational Assistant

console.log('TopicFlow JavaScript loaded');

// ============================================================================
// PDF Upload Handling
// ============================================================================

// Store uploaded PDF file
let uploadedPdfFile = null;

/**
 * Handle PDF file upload
 * @param {Event} event - File input change event
 */
function handlePdfUpload(event) {
    const file = event.target.files[0];
    
    if (!file) {
        return;
    }
    
    // Validate file type
    if (!file.name.toLowerCase().endsWith('.pdf')) {
        showNotification('✗ Only PDF files are supported', 'error');
        event.target.value = '';
        return;
    }
    
    // Validate file size (16MB max)
    const maxSize = 16 * 1024 * 1024; // 16MB in bytes
    if (file.size > maxSize) {
        showNotification('✗ File size exceeds 16MB limit', 'error');
        event.target.value = '';
        return;
    }
    
    // Store the file
    uploadedPdfFile = file;
    
    // Update UI
    document.getElementById('pdf-filename').classList.remove('hidden');
    document.getElementById('pdf-name').textContent = file.name;
    document.getElementById('clear-pdf-btn').classList.remove('hidden');
    
    // Clear text input when PDF is uploaded
    const materialInput = document.getElementById('material-input');
    materialInput.value = '';
    materialInput.placeholder = 'PDF file selected. You can also add additional text here...';
    
    // Enable buttons
    updateButtonState();
    
    showNotification('✓ PDF file loaded successfully!');
}

/**
 * Clear PDF upload
 */
function clearPdfUpload() {
    uploadedPdfFile = null;
    
    const fileInput = document.getElementById('pdf-upload');
    fileInput.value = '';
    
    document.getElementById('pdf-filename').classList.add('hidden');
    document.getElementById('clear-pdf-btn').classList.add('hidden');
    
    const materialInput = document.getElementById('material-input');
    materialInput.placeholder = 'Enter your study material here... (e.g., lecture notes, textbook excerpts, study guides) OR upload a PDF file above';
    
    updateButtonState();
    
    showNotification('✓ PDF file cleared');
}

// ============================================================================
// Tab Navigation System
// ============================================================================

/**
 * Switch between tabs in the application
 * @param {string} tabName - Name of the tab to switch to
 */
function switchTab(tabName) {
    // Hide all content panels
    const panels = document.querySelectorAll('.content-panel');
    panels.forEach(panel => {
        panel.classList.add('hidden');
    });

    // Remove active state from all tab buttons
    const tabs = document.querySelectorAll('.tab-button');
    tabs.forEach(tab => {
        tab.classList.remove('bg-blue-600', 'text-white');
        tab.classList.add('text-gray-600', 'hover:bg-gray-100');
    });

    // Show selected panel
    const selectedPanel = document.getElementById(`panel-${tabName}`);
    if (selectedPanel) {
        selectedPanel.classList.remove('hidden');
        selectedPanel.classList.add('fade-in');
    }

    // Activate selected tab button
    const selectedTab = document.getElementById(`tab-${tabName}`);
    if (selectedTab) {
        selectedTab.classList.add('bg-blue-600', 'text-white');
        selectedTab.classList.remove('text-gray-600', 'hover:bg-gray-100');
    }
}

// ============================================================================
// Input Validation and Button State Management
// ============================================================================

/**
 * Update submit button state based on input validation
 */
function updateButtonState() {
    const materialInput = document.getElementById('material-input');
    const material = materialInput.value.trim();
    const hasPdf = uploadedPdfFile !== null;
    const isValid = material.length > 0 || hasPdf;

    // Update all submit buttons
    const buttons = [
        'btn-summarize',
        'btn-summarize-2',
        'btn-quiz',
        'btn-quiz-2',
        'btn-flashcard',
        'btn-flashcard-2'
    ];

    buttons.forEach(btnId => {
        const btn = document.getElementById(btnId);
        if (btn) {
            btn.disabled = !isValid;
        }
    });

    // Update character count
    const charCount = document.getElementById('char-count');
    if (charCount) {
        if (hasPdf) {
            charCount.textContent = `PDF: ${uploadedPdfFile.name}`;
        } else {
            charCount.textContent = materialInput.value.length;
        }
    }
}

// ============================================================================
// API Call Utilities
// ============================================================================

/**
 * Make API call to backend
 * @param {string} endpoint - API endpoint path
 * @param {object} data - Data to send
 * @param {File} file - Optional file to upload
 * @returns {Promise<object>} - Response data
 */
async function callAPI(endpoint, data, file = null) {
    console.log('callAPI called:', { endpoint, hasFile: !!file, data });
    
    let response;
    
    try {
        if (file) {
            console.log('Preparing FormData with file:', file.name);
            // Use FormData for file upload
            const formData = new FormData();
            formData.append('pdf_file', file);
            
            // Add any additional text data if present
            if (data && data.material) {
                formData.append('material', data.material);
            }
            
            console.log('Sending POST request with FormData to:', endpoint);
            response = await fetch(endpoint, {
                method: 'POST',
                body: formData
            });
        } else {
            console.log('Sending POST request with JSON to:', endpoint);
            // Use JSON for regular requests
            response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
        }

        console.log('Response status:', response.status);
        console.log('Response ok:', response.ok);

        // Read response body once
        const responseText = await response.text();
        console.log('Response text length:', responseText.length);
        
        if (!response.ok) {
            // Try to parse error as JSON
            let errorMessage;
            try {
                const errorData = JSON.parse(responseText);
                errorMessage = errorData.error || `HTTP ${response.status}`;
            } catch (e) {
                // If JSON parsing fails, use text
                errorMessage = responseText || `HTTP ${response.status}`;
            }
            throw new Error(errorMessage);
        }

        // Try to parse response as JSON
        try {
            return JSON.parse(responseText);
        } catch (e) {
            console.error('Failed to parse JSON response:', e);
            console.error('Response text:', responseText);
            throw new Error('Invalid JSON response from server. Check console for details.');
        }
    } catch (error) {
        console.error('API call error:', error);
        throw error;
    }
}

/**
 * Show loading indicator for a feature
 * @param {string} feature - Feature name (summarizer, quiz, flashcard)
 */
function showLoading(feature) {
    const loading = document.getElementById(`loading-${feature}`);
    const results = document.getElementById(`results-${feature}`);
    const error = document.getElementById(`error-${feature}`);

    if (loading) loading.classList.remove('hidden');
    if (results) results.classList.add('hidden');
    if (error) error.classList.add('hidden');
}

/**
 * Hide loading indicator for a feature
 * @param {string} feature - Feature name (summarizer, quiz, flashcard)
 */
function hideLoading(feature) {
    const loading = document.getElementById(`loading-${feature}`);
    if (loading) loading.classList.add('hidden');
}

/**
 * Show error message for a feature
 * @param {string} feature - Feature name (summarizer, quiz, flashcard)
 * @param {string} message - Error message to display
 */
function showError(feature, message) {
    const error = document.getElementById(`error-${feature}`);
    const errorText = document.getElementById(`error-${feature}-text`);

    if (error && errorText) {
        errorText.textContent = message;
        error.classList.remove('hidden');
    }
}

/**
 * Show results for a feature
 * @param {string} feature - Feature name (summarizer, quiz, flashcard)
 */
function showResults(feature) {
    const results = document.getElementById(`results-${feature}`);
    if (results) {
        results.classList.remove('hidden');
        results.classList.add('fade-in');
    }
}

// ============================================================================
// AI Summarizer
// ============================================================================

/**
 * Submit material to the summarizer API
 */
async function submitSummarizer() {
    console.log('submitSummarizer called');
    
    const materialInput = document.getElementById('material-input');
    const material = materialInput.value.trim();

    console.log('Material length:', material.length);
    console.log('Uploaded PDF:', uploadedPdfFile);

    // Check if we have either text or PDF
    if (!material && !uploadedPdfFile) {
        showError('summarizer', 'Please enter study material or upload a PDF file before submitting.');
        return;
    }

    try {
        showLoading('summarizer');
        
        let data;
        
        console.log('Calling API with PDF:', !!uploadedPdfFile);
        
        // If PDF is uploaded, use file upload
        if (uploadedPdfFile) {
            console.log('Using PDF upload mode');
            data = await callAPI('/api/summarize', { material }, uploadedPdfFile);
        } else {
            // Otherwise use text input
            console.log('Using text input mode');
            data = await callAPI('/api/summarize', { material });
        }
        
        console.log('Summarizer response:', data); // Debug log
        
        hideLoading('summarizer');
        
        // Render summary - pass the entire data object or just the summary field
        if (data && data.summary) {
            renderSummary(data.summary);
            
            // Save to history
            const historyMaterial = uploadedPdfFile 
                ? `PDF: ${uploadedPdfFile.name}` 
                : material.substring(0, 100) + '...';
            
            saveToHistory('summary', {
                material: historyMaterial,
                result: data.summary,
                timestamp: new Date().toISOString()
            });
        } else {
            // Fallback if structure is different
            renderSummary(data);
        }
        
        showResults('summarizer');
        
        // Switch to summarizer tab
        switchTab('summarizer');
        
    } catch (error) {
        console.error('Summarizer error:', error); // Debug log
        hideLoading('summarizer');
        showError('summarizer', error.message || 'Failed to generate summary. Please try again.');
    }
}

// ============================================================================
// History Management
// ============================================================================

/**
 * Save result to history
 */
function saveToHistory(type, data) {
    try {
        let history = JSON.parse(localStorage.getItem('topicflow_history') || '[]');
        
        // Add new entry
        history.unshift({
            type: type,
            data: data,
            id: Date.now()
        });
        
        // Keep only last 10 entries
        history = history.slice(0, 10);
        
        localStorage.setItem('topicflow_history', JSON.stringify(history));
    } catch (e) {
        console.error('Failed to save history:', e);
    }
}

/**
 * Get history
 */
function getHistory() {
    try {
        return JSON.parse(localStorage.getItem('topicflow_history') || '[]');
    } catch (e) {
        return [];
    }
}

/**
 * Clear history
 */
function clearHistory() {
    const lang = localStorage.getItem('language') || 'en';
    const confirmMsg = lang === 'id' 
        ? 'Apakah Anda yakin ingin menghapus semua riwayat?' 
        : 'Are you sure you want to clear all history?';
    
    if (confirm(confirmMsg)) {
        localStorage.removeItem('topicflow_history');
        showNotification(lang === 'id' ? '✓ Riwayat berhasil dihapus!' : '✓ History cleared successfully!');
        renderHistoryPanel(); // Refresh panel
    }
}

/**
 * Toggle history panel
 */
function toggleHistoryPanel() {
    const panel = document.getElementById('history-panel');
    const isHidden = panel.classList.contains('hidden');
    
    if (isHidden) {
        panel.classList.remove('hidden');
        renderHistoryPanel();
    } else {
        panel.classList.add('hidden');
    }
}

/**
 * Render history panel
 */
function renderHistoryPanel() {
    const container = document.getElementById('history-content');
    const history = getHistory();
    const lang = localStorage.getItem('language') || 'en';
    
    if (history.length === 0) {
        container.innerHTML = `
            <div class="text-center py-12 text-gray-500">
                <p class="text-4xl mb-4">📭</p>
                <p class="text-lg">${lang === 'id' ? 'Belum ada riwayat' : 'No history yet'}</p>
                <p class="text-sm mt-2">${lang === 'id' ? 'Generate summary, quiz, atau flashcard untuk menyimpan riwayat' : 'Generate summaries, quizzes, or flashcards to save history'}</p>
            </div>
        `;
        return;
    }
    
    let html = '<div class="space-y-4">';
    
    history.forEach((item, index) => {
        const date = new Date(item.data.timestamp);
        const typeIcon = item.type === 'summary' ? '📋' : item.type === 'quiz' ? '❓' : '🎴';
        const typeName = item.type === 'summary' 
            ? (lang === 'id' ? 'Ringkasan' : 'Summary')
            : item.type === 'quiz' 
            ? (lang === 'id' ? 'Kuis' : 'Quiz')
            : (lang === 'id' ? 'Flashcard' : 'Flashcard');
        
        html += `
            <div class="bg-gray-50 dark:bg-gray-700 rounded-lg p-4 border-l-4 ${
                item.type === 'summary' ? 'border-blue-500' : 
                item.type === 'quiz' ? 'border-purple-500' : 'border-pink-500'
            }">
                <div class="flex justify-between items-start mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-2xl">${typeIcon}</span>
                        <div>
                            <h3 class="font-semibold text-gray-800 dark:text-gray-200">${typeName}</h3>
                            <p class="text-xs text-gray-500 dark:text-gray-400">${date.toLocaleString()}</p>
                        </div>
                    </div>
                    <button onclick="deleteHistoryItem(${item.id})" class="text-red-600 hover:text-red-700 px-2 py-1">
                        🗑️
                    </button>
                </div>
                <p class="text-sm text-gray-600 dark:text-gray-300 mb-2">
                    <strong>${lang === 'id' ? 'Materi:' : 'Material:'}</strong> ${escapeHtml(item.data.material)}
                </p>
                <details class="text-sm">
                    <summary class="cursor-pointer text-blue-600 hover:text-blue-700">
                        ${lang === 'id' ? 'Lihat hasil' : 'View result'}
                    </summary>
                    <div class="mt-2 p-3 bg-white dark:bg-gray-800 rounded border border-gray-200 dark:border-gray-600 max-h-40 overflow-y-auto">
                        <pre class="whitespace-pre-wrap text-xs">${escapeHtml(item.data.result.substring(0, 500))}${item.data.result.length > 500 ? '...' : ''}</pre>
                    </div>
                </details>
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
}

/**
 * Delete history item
 */
function deleteHistoryItem(id) {
    try {
        let history = getHistory();
        history = history.filter(item => item.id !== id);
        localStorage.setItem('topicflow_history', JSON.stringify(history));
        renderHistoryPanel();
        
        const lang = localStorage.getItem('language') || 'en';
        showNotification(lang === 'id' ? '✓ Item dihapus' : '✓ Item deleted');
    } catch (e) {
        console.error('Failed to delete history item:', e);
    }
}

/**
 * Render summary in bulleted format
 * @param {string|object} summaryData - Summary text or object to render
 */
function renderSummary(summaryData) {
    const container = document.getElementById('summary-content');
    
    // Handle different response formats
    let summaryText = '';
    if (typeof summaryData === 'string') {
        summaryText = summaryData;
    } else if (summaryData && typeof summaryData === 'object') {
        // If it's an object, try to extract the summary field
        summaryText = summaryData.summary || summaryData.text || summaryData.content || '';
    } else {
        summaryText = String(summaryData || '');
    }
    
    // Check if summary is empty or null
    if (!summaryText || summaryText.trim() === '' || summaryText === 'null') {
        container.innerHTML = `
            <div class="bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
                <p class="text-yellow-800">
                    <strong>No summary generated.</strong> The AI returned an empty response. 
                    Please try again with different material or wait a moment and retry.
                </p>
            </div>
        `;
        return;
    }
    
    // Split by newlines and create bullet points
    const lines = summaryText.split('\n').filter(line => line.trim() && line.trim() !== 'null');
    
    if (lines.length === 0) {
        container.innerHTML = `
            <div class="bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
                <p class="text-yellow-800">
                    <strong>No content to display.</strong> Please try generating the summary again.
                </p>
            </div>
        `;
        return;
    }
    
    let html = '<div class="mb-4 flex flex-wrap gap-2">';
    html += '<button onclick="copySummary()" class="flex-1 min-w-[120px] sm:flex-none px-3 md:px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center gap-1 md:gap-2 text-xs md:text-sm">';
    html += '<span>📋</span> <span data-i18n="copy">Copy</span>';
    html += '</button>';
    html += '<button onclick="exportSummary()" class="flex-1 min-w-[120px] sm:flex-none px-3 md:px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-all flex items-center justify-center gap-1 md:gap-2 text-xs md:text-sm">';
    html += '<span>💾</span> <span data-i18n="exportText">Export Text</span>';
    html += '</button>';
    html += '<button onclick="exportSummaryPDF()" class="flex-1 min-w-[120px] sm:flex-none px-3 md:px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-all flex items-center justify-center gap-1 md:gap-2 text-xs md:text-sm">';
    html += '<span>📄</span> <span data-i18n="exportPDF">Export PDF</span>';
    html += '</button>';
    html += '<button onclick="printSummary()" class="flex-1 min-w-[120px] sm:flex-none px-3 md:px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-all flex items-center justify-center gap-1 md:gap-2 text-xs md:text-sm">';
    html += '<span>🖨️</span> <span data-i18n="print">Print</span>';
    html += '</button>';
    html += '</div>';
    
    html += '<ul class="space-y-2" id="summary-list">';
    lines.forEach(line => {
        // Remove existing bullet points if any
        const cleanLine = line.replace(/^[•\-\*]\s*/, '').trim();
        if (cleanLine && cleanLine !== 'null') {
            html += `<li class="flex items-start">
                <span class="text-blue-600 mr-2">•</span>
                <span class="text-gray-700">${escapeHtml(cleanLine)}</span>
            </li>`;
        }
    });
    html += '</ul>';
    
    container.innerHTML = html;
    
    // Store summary for export
    window.currentSummary = summaryText;
}

/**
 * Copy summary to clipboard
 */
function copySummary() {
    if (!window.currentSummary) return;
    
    navigator.clipboard.writeText(window.currentSummary).then(() => {
        showNotification('✓ Summary copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy:', err);
        showNotification('✗ Failed to copy to clipboard', 'error');
    });
}

/**
 * Export summary as text file
 */
function exportSummary() {
    if (!window.currentSummary) return;
    
    const blob = new Blob([window.currentSummary], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `topicflow-summary-${Date.now()}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showNotification('✓ Summary exported successfully!');
}

/**
 * Export summary as PDF file
 */
function exportSummaryPDF() {
    if (!window.currentSummary) return;
    
    try {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        
        // Add title
        doc.setFontSize(20);
        doc.setTextColor(59, 130, 246); // Blue color
        doc.text('TopicFlow - AI Summary', 20, 20);
        
        // Add date
        doc.setFontSize(10);
        doc.setTextColor(100, 100, 100);
        doc.text(`Generated: ${new Date().toLocaleString()}`, 20, 30);
        
        // Add line
        doc.setDrawColor(59, 130, 246);
        doc.line(20, 35, 190, 35);
        
        // Add summary content
        doc.setFontSize(12);
        doc.setTextColor(0, 0, 0);
        
        const lines = doc.splitTextToSize(window.currentSummary, 170);
        doc.text(lines, 20, 45);
        
        // Add footer
        const pageCount = doc.internal.getNumberOfPages();
        for (let i = 1; i <= pageCount; i++) {
            doc.setPage(i);
            doc.setFontSize(8);
            doc.setTextColor(150, 150, 150);
            doc.text(
                `TopicFlow - M Rizki Agil Prakoso & Imam Agus Faisal - Page ${i} of ${pageCount}`,
                105,
                285,
                { align: 'center' }
            );
        }
        
        // Save PDF
        doc.save(`topicflow-summary-${Date.now()}.pdf`);
        
        showNotification('✓ PDF exported successfully!');
    } catch (error) {
        console.error('PDF export error:', error);
        showNotification('✗ Failed to export PDF', 'error');
    }
}

/**
 * Print summary
 */
function printSummary() {
    if (!window.currentSummary) return;
    
    const printWindow = window.open('', '', 'width=800,height=600');
    printWindow.document.write(`
        <html>
        <head>
            <title>TopicFlow Summary</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; }
                h1 { color: #3b82f6; }
                ul { line-height: 1.8; }
                .footer { margin-top: 40px; color: #666; font-size: 12px; }
            </style>
        </head>
        <body>
            <h1>TopicFlow - AI Summary</h1>
            <p><strong>Generated:</strong> ${new Date().toLocaleString()}</p>
            <hr>
            <div style="white-space: pre-wrap;">${escapeHtml(window.currentSummary)}</div>
            <div class="footer">
                <p>Generated by TopicFlow - AI Educational Assistant</p>
                <p>Developers: M Rizki Agil Prakoso & Imam Agus Faisal</p>
            </div>
        </body>
        </html>
    `);
    printWindow.document.close();
    printWindow.print();
}

/**
 * Show notification message
 */
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 px-6 py-3 rounded-lg shadow-lg z-50 ${
        type === 'success' ? 'bg-green-600' : 'bg-red-600'
    } text-white font-medium animate-fade-in`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transition = 'opacity 0.3s';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// ============================================================================
// AI Quiz Generator
// ============================================================================

/**
 * Submit material to the quiz generator API
 */
async function submitQuiz() {
    const materialInput = document.getElementById('material-input');
    const material = materialInput.value.trim();

    // Check if we have either text or PDF
    if (!material && !uploadedPdfFile) {
        showError('quiz', 'Please enter study material or upload a PDF file before submitting.');
        return;
    }

    try {
        showLoading('quiz');
        
        let data;
        
        // If PDF is uploaded, use file upload
        if (uploadedPdfFile) {
            data = await callAPI('/api/quiz', { material }, uploadedPdfFile);
        } else {
            // Otherwise use text input
            data = await callAPI('/api/quiz', { material });
        }
        
        hideLoading('quiz');
        
        // Render quiz
        renderQuiz(data.questions);
        showResults('quiz');
        
        // Switch to quiz tab
        switchTab('quiz');
        
    } catch (error) {
        hideLoading('quiz');
        showError('quiz', error.message || 'Failed to generate quiz. Please try again.');
    }
}

/**
 * Render quiz questions
 * @param {Array} questions - Array of question objects
 */
function renderQuiz(questions) {
    const container = document.getElementById('quiz-content');
    
    // Validate questions is an array
    if (!Array.isArray(questions)) {
        container.innerHTML = '<p class="text-red-600">Error: Invalid quiz data format</p>';
        return;
    }
    
    let html = '';
    questions.forEach((q, index) => {
        // Validate question object
        if (!q || typeof q !== 'object') {
            return;
        }
        
        const question = q.question || 'Question not available';
        const choices = Array.isArray(q.choices) ? q.choices : [];
        const correctAnswer = q.correct_answer || '';
        const explanation = q.explanation || 'No explanation available';
        
        html += `
            <div class="bg-gray-50 rounded-lg p-6 border-2 border-gray-200">
                <h4 class="font-semibold text-lg text-gray-800 mb-4">
                    Question ${index + 1}: ${escapeHtml(question)}
                </h4>
                <div class="space-y-2 mb-4">
                    ${choices.map((choice, choiceIndex) => `
                        <div 
                            class="answer-choice p-3 border-2 border-gray-300 rounded-lg cursor-pointer"
                            onclick="selectAnswer(${index}, ${choiceIndex}, '${escapeHtml(correctAnswer)}', '${escapeHtml(choice)}')">
                            <span class="font-medium">${String.fromCharCode(65 + choiceIndex)}.</span> ${escapeHtml(choice)}
                        </div>
                    `).join('')}
                </div>
                <div id="explanation-${index}" class="hidden bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
                    <p class="text-sm font-medium text-blue-900 mb-1">Explanation:</p>
                    <p class="text-sm text-blue-800">${escapeHtml(explanation)}</p>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
    
    // Update score display
    const scoreDisplay = document.getElementById('quiz-score');
    scoreDisplay.textContent = `0 / ${questions.length} answered`;
}

/**
 * Escape HTML to prevent XSS
 * @param {string} text - Text to escape
 * @returns {string} - Escaped text
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Handle answer selection
 * @param {number} questionIndex - Index of the question
 * @param {number} choiceIndex - Index of the selected choice
 * @param {string} correctAnswer - The correct answer text
 * @param {string} selectedAnswer - The selected answer text
 */
function selectAnswer(questionIndex, choiceIndex, correctAnswer, selectedAnswer) {
    const questionDiv = document.getElementById('quiz-content').children[questionIndex];
    const choices = questionDiv.querySelectorAll('.answer-choice');
    
    // Disable all choices
    choices.forEach(choice => {
        choice.style.pointerEvents = 'none';
    });
    
    // Mark selected answer
    choices[choiceIndex].classList.add('selected');
    
    // Highlight correct and incorrect answers
    choices.forEach((choice, idx) => {
        const choiceText = choice.textContent.trim().substring(3); // Remove "A. ", "B. ", etc.
        if (choiceText === correctAnswer) {
            choice.classList.add('correct');
        } else if (idx === choiceIndex && choiceText !== correctAnswer) {
            choice.classList.add('incorrect');
        }
    });
    
    // Show explanation
    const explanation = document.getElementById(`explanation-${questionIndex}`);
    explanation.classList.remove('hidden');
    
    // Update score
    updateQuizScore();
}

/**
 * Update quiz score display
 */
function updateQuizScore() {
    const container = document.getElementById('quiz-content');
    const totalQuestions = container.children.length;
    const answeredQuestions = container.querySelectorAll('.answer-choice.selected').length;
    
    const scoreDisplay = document.getElementById('quiz-score');
    scoreDisplay.textContent = `${answeredQuestions} / ${totalQuestions} answered`;
}

// ============================================================================
// AI Flashcard Maker
// ============================================================================

/**
 * Submit material to the flashcard maker API
 */
async function submitFlashcard() {
    const materialInput = document.getElementById('material-input');
    const material = materialInput.value.trim();

    // Check if we have either text or PDF
    if (!material && !uploadedPdfFile) {
        showError('flashcard', 'Please enter study material or upload a PDF file before submitting.');
        return;
    }

    try {
        showLoading('flashcard');
        
        let data;
        
        // If PDF is uploaded, use file upload
        if (uploadedPdfFile) {
            data = await callAPI('/api/flashcard', { material }, uploadedPdfFile);
        } else {
            // Otherwise use text input
            data = await callAPI('/api/flashcard', { material });
        }
        
        hideLoading('flashcard');
        
        // Render flashcards
        renderFlashcards(data.flashcards);
        showResults('flashcard');
        
        // Switch to flashcard tab
        switchTab('flashcard');
        
    } catch (error) {
        hideLoading('flashcard');
        showError('flashcard', error.message || 'Failed to generate flashcards. Please try again.');
    }
}

/**
 * Render flashcards
 * @param {Array} flashcards - Array of flashcard objects
 */
function renderFlashcards(flashcards) {
    const container = document.getElementById('flashcard-content');
    
    // Validate flashcards is an array
    if (!Array.isArray(flashcards)) {
        container.innerHTML = '<p class="text-red-600">Error: Invalid flashcard data format</p>';
        return;
    }
    
    let html = '';
    flashcards.forEach((card, index) => {
        // Validate card object
        if (!card || typeof card !== 'object') {
            return;
        }
        
        const term = card.term || 'Term not available';
        const definition = card.definition || 'Definition not available';
        
        html += `
            <div class="flashcard h-64" onclick="flipCard(${index})">
                <div class="flashcard-inner" id="flashcard-${index}">
                    <div class="flashcard-front">
                        <div class="text-center">
                            <p class="text-sm uppercase tracking-wide mb-2 opacity-75">Term</p>
                            <p class="text-xl font-bold">${escapeHtml(term)}</p>
                        </div>
                    </div>
                    <div class="flashcard-back">
                        <div class="text-center">
                            <p class="text-sm uppercase tracking-wide mb-2 opacity-75">Definition</p>
                            <p class="text-lg">${escapeHtml(definition)}</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

/**
 * Flip a flashcard
 * @param {number} index - Index of the flashcard to flip
 */
function flipCard(index) {
    const card = document.getElementById(`flashcard-${index}`).parentElement;
    card.classList.toggle('flipped');
}

// ============================================================================
// Multi-Language Support
// ============================================================================

const translations = {
    en: {
        subtitle: 'AI-Powered Educational Assistant',
        description: 'Transform your study materials into summaries, quizzes, and flashcards',
        history: 'History',
        historyTitle: '📚 History',
        clearHistory: 'Clear All',
        close: 'Close',
        copy: 'Copy',
        exportText: 'Export Text',
        exportPDF: 'Export PDF',
        print: 'Print',
        materialInput: 'Material Input',
        summarizer: 'Summarizer',
        quiz: 'Quiz Generator',
        flashcard: 'Flashcards',
        about: 'About'
    },
    id: {
        subtitle: 'Asisten Pendidikan Berbasis AI',
        description: 'Ubah materi belajar Anda menjadi ringkasan, kuis, dan flashcard',
        history: 'Riwayat',
        historyTitle: '📚 Riwayat',
        clearHistory: 'Hapus Semua',
        close: 'Tutup',
        copy: 'Salin',
        exportText: 'Ekspor Teks',
        exportPDF: 'Ekspor PDF',
        print: 'Cetak',
        materialInput: 'Input Materi',
        summarizer: 'Peringkas',
        quiz: 'Pembuat Kuis',
        flashcard: 'Kartu Belajar',
        about: 'Tentang'
    }
};

/**
 * Toggle language
 */
function toggleLanguage() {
    const currentLang = localStorage.getItem('language') || 'en';
    const newLang = currentLang === 'en' ? 'id' : 'en';
    
    localStorage.setItem('language', newLang);
    applyLanguage(newLang);
    
    showNotification(newLang === 'id' ? '✓ Bahasa diubah ke Indonesia' : '✓ Language changed to English');
}

/**
 * Apply language to all elements
 */
function applyLanguage(lang) {
    // Update language toggle button
    const langText = document.getElementById('lang-text');
    if (langText) {
        langText.textContent = lang.toUpperCase();
    }
    
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
}

/**
 * Load language preference
 */
function loadLanguagePreference() {
    const lang = localStorage.getItem('language') || 'en';
    applyLanguage(lang);
}

// ============================================================================
// Dark Mode Toggle
// ============================================================================

/**
 * Toggle dark mode
 */
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    
    // Update icon
    const icon = document.getElementById('dark-mode-icon');
    if (icon) icon.textContent = isDark ? '☀️' : '🌙';
    
    // Save preference
    localStorage.setItem('darkMode', isDark ? 'enabled' : 'disabled');
    
    showNotification(isDark ? '🌙 Dark mode enabled' : '☀️ Light mode enabled');
}

/**
 * Load dark mode preference
 */
function loadDarkModePreference() {
    const darkMode = localStorage.getItem('darkMode');
    
    // Default to dark mode if no preference is set
    if (darkMode === null || darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
        const icon = document.getElementById('dark-mode-icon');
        if (icon) icon.textContent = '☀️';
        
        // Save default preference if not set
        if (darkMode === null) {
            localStorage.setItem('darkMode', 'enabled');
        }
    } else {
        // Light mode
        document.body.classList.remove('dark-mode');
        const icon = document.getElementById('dark-mode-icon');
        if (icon) icon.textContent = '🌙';
    }
}

// ============================================================================
// Initialization
// ============================================================================

// Initialize application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('TopicFlow application initialized');
    
    // Load preferences
    loadDarkModePreference();
    loadLanguagePreference();
    
    // Add event listener to material input
    const materialInput = document.getElementById('material-input');
    if (materialInput) {
        materialInput.addEventListener('input', updateButtonState);
        
        // Initial button state
        updateButtonState();
    }
    
    // Set initial tab
    switchTab('material');
    
    // Close history panel when clicking outside
    document.getElementById('history-panel').addEventListener('click', function(e) {
        if (e.target === this) {
            toggleHistoryPanel();
        }
    });
});