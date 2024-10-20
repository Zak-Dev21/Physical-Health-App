document.getElementById('addTask').addEventListener('click', function() {
    const taskInput = document.createElement('input');
    taskInput.type = 'text';
    taskInput.placeholder = 'Task Description';
    document.getElementById('tasks').appendChild(taskInput);
});

document.getElementById('scheduleForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect user data
    const jobType = document.getElementById('jobType').value;
    const activityLevel = document.getElementById('activityLevel').value.toLowerCase();
    const goals = document.getElementById('goals').value.toLowerCase();

    // Generate workout suggestions based on user input
    const workoutSuggestions = generateWorkoutSuggestions(jobType, activityLevel, goals);
    // Generate timing suggestions based on user input
    const timingSuggestions = generateTimingSuggestions(activityLevel, goals);

    // Display the workout suggestions
    const workoutSuggestionsDiv = document.getElementById('workoutSuggestions');
    workoutSuggestionsDiv.innerHTML = "<h3>Workout Suggestions</h3>";
    
    workoutSuggestions.forEach(suggestion => {
        const suggestionElement = document.createElement('p');
        suggestionElement.textContent = suggestion;
        workoutSuggestionsDiv.appendChild(suggestionElement);
    });

    // Display timing suggestions
    workoutSuggestionsDiv.innerHTML += "<h3>Suggested Timing</h3>";
    timingSuggestions.forEach(timing => {
        const timingElement = document.createElement('p');
        timingElement.textContent = timing;
        workoutSuggestionsDiv.appendChild(timingElement);
    });

    // Clear the input fields
    document.getElementById('scheduleForm').reset();
});

// Function to generate workout suggestions based on user input
function generateWorkoutSuggestions(jobType, activityLevel, goals) {
    const suggestions = [];

    // Example logic for generating suggestions
    if (activityLevel === "high") {
        suggestions.push("Try interval training to maximize your efficiency.");
        suggestions.push("Incorporate strength training twice a week.");
    } else if (activityLevel === "medium") {
        suggestions.push("Consider a balanced mix of cardio and strength training.");
        suggestions.push("Aim for at least 150 minutes of moderate activity each week.");
    } else {
        suggestions.push("Start with light exercises, such as walking or yoga.");
        suggestions.push("Gradually increase your activity level over time.");
    }

    // Add suggestions based on goals as needed
    if (goals.includes("weight loss")) {
        suggestions.push("Focus on high-intensity interval training (HIIT) for weight loss.");
    }

    return suggestions;
}

// Function to generate timing suggestions based on user input
function generateTimingSuggestions(activityLevel, goals) {
    const timingSuggestions = [];

    // Add timing suggestions based on activity level
    if (activityLevel === "high") {
        timingSuggestions.push("Schedule workouts in the morning before work for maximum energy.");
        timingSuggestions.push("Try short sessions during lunch breaks.");
    } else if (activityLevel === "medium") {
        timingSuggestions.push("Consider evening workouts after work when your energy levels are higher.");
    } else {
        timingSuggestions.push("Short sessions in the evening or weekends are best to ease into exercise.");
    }

    // Additional timing suggestions based on goals
    if (goals.includes("weight loss")) {
        timingSuggestions.push("Aim for workouts in the evening to help boost metabolism.");
    } else if (goals.includes("muscle gain")) {
        timingSuggestions.push("Morning workouts can maximize energy for strength training.");
    } else if (goals.includes("flexibility")) {
        timingSuggestions.push("Evening or morning yoga sessions can be beneficial.");
    }

    return timingSuggestions;
}

