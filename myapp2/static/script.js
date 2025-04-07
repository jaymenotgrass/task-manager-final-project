function filterTasks() {
    // Get the search term from the input field
    var searchTerm = document.getElementById("task-search").value.toLowerCase();
    
    // Get all the task items
    var taskItems = document.querySelectorAll(".task-item");

    // Loop through each task and check if it matches the search term
    taskItems.forEach(function(item) {
        // Get the task name and description
        var taskName = item.getAttribute("data-name").toLowerCase();
        var taskDescription = item.getAttribute("data-description").toLowerCase();

        // If the task name or description includes the search term, show the task; otherwise, hide it
        if (taskName.includes(searchTerm) || taskDescription.includes(searchTerm)) {
            item.style.display = "block";  // Show task
        } else {
            item.style.display = "none";   // Hide task
        }
    });
}