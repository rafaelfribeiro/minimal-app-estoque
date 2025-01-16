document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const recordId = this.getAttribute('data-id');
            const confirmation = confirm('Are you sure you want to delete this record?');
            if (confirmation) {
                fetch(`/delete/${recordId}`, {
                    method: 'DELETE'
                }).then(response => {
                    if (response.ok) {
                        alert('Record deleted successfully.');
                        location.reload();
                    } else {
                        alert('Error deleting record.');
                    }
                });
            }
        });
    });
});