/**
 * Weekly Wellness Newsletter Generator
 * Main JavaScript file
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Weekly Wellness Newsletter Generator initialized');
    
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Handle form submission for newsletter sending
    const sendForm = document.querySelector('form[action*="send"]');
    if (sendForm) {
        sendForm.addEventListener('submit', function(event) {
            const recipients = document.getElementById('recipients').value;
            if (!recipients.trim()) {
                event.preventDefault();
                alert('Please enter at least one recipient email address.');
                return false;
            }
            
            // Validate email addresses
            const emails = recipients.split(',').map(email => email.trim());
            const invalidEmails = emails.filter(email => !isValidEmail(email));
            
            if (invalidEmails.length > 0) {
                event.preventDefault();
                alert(`The following email addresses are invalid: ${invalidEmails.join(', ')}`);
                return false;
            }
            
            // Add loading state to the submit button
            const submitButton = sendForm.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Sending...';
                submitButton.disabled = true;
            }
            
            return true;
        });
    }
    
    // Function to validate email address format
    function isValidEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
    
    // Handle newsletter settings form
    const settingsForm = document.querySelector('form:not([action])');
    if (settingsForm) {
        const saveButton = settingsForm.querySelector('button[type="button"]');
        if (saveButton) {
            saveButton.addEventListener('click', function() {
                alert('Settings saved functionality is part of the premium version.');
            });
        }
    }
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Add animation to cards
    const cards = document.querySelectorAll('.card-dashboard');
    cards.forEach(function(card) {
        card.classList.add('fade-in');
    });
});
