// DESTROY THE UI BAR
UIBar.destroy();

// UNDO BUTTON
$(document).on(":start", function () {
  // Check if 'enableUndo' is stored in localStorage, set it to 'false' if not.
  if (localStorage.getItem("enableUndo") === null) {
    localStorage.setItem("enableUndo", "false"); // Set default to false if not present
  }

  // Load the enableUndo state from localStorage
  State.variables.enableUndo = localStorage.getItem("enableUndo") === "true";

  // Update the undo button based on the current state.
  updateUndoButton();
});

setup.enableUndo = {
  // Retrieves the current undo state from localStorage, defaulting to false
  get: function () {
    return localStorage.getItem("enableUndo") === "true";
  },

  // Toggles the undo state and saves the new state to localStorage
  toggle: function () {
    var currentState = this.get();
    localStorage.setItem("enableUndo", !currentState);
    State.variables.enableUndo = !currentState;

    // Refresh the current passage to reflect the change immediately
    Engine.play(passage());
  },
};

function updateUndoButton() {
  $("#undobar").remove(); // Remove existing Undo button, if any.

  if (setup.enableUndo.get()) {
    // Show the undo button
    $("body").prepend(
      "<div id='undobar'><a href='#' id='undoButton'>←</a></div>"
    );

    $("#undoButton").on("click", function (e) {
      e.preventDefault();
      Engine.backward();
    });
  }
}

// Attached to :passagerender event to initialize on passage render

// Initialize the undo button on passage render
$(document).on(":passagerender", updateUndoButton);

// AUTOSAVE
// Autosaves whenever you enter a new passage
$(document).on(":passagerender", function () {
  // Check if the current passage is not a certain passage
  if (
    State.passage !== "Start" &&
    State.passage !== "options" &&
    State.passage !== "content_warning" &&
    State.passage !== "its_okay" &&
    State.passage !== "restart"
  ) {
    Save.slots.save(1); // Automatically save to slot 1
  }
});

// CSS CHANGES FOR #PASSAGES AND LINKS
// I can't change the #passages sections with Twine tags alone
$(document).on(":passagerender", function (ev) {
  // Get the current passage's tags
  var currentTags = tags();

  // Check if tag is included
  if (currentTags.includes("flashback")) {
    // Apply styles for passages with the tag
    $("#passages").css({
      "background-color": "transparent",
      "box-shadow": "none",
      color: "black",
    });
  } else if (currentTags.includes("options")) {
    $("#passages").css({
      "background-color": "rgb(27 27 27)",
      "box-shadow": "var(--shadow-elevation-high)",
    });
  } else {
    // Reset styles for passages without certain tags
    $("#passages").css({
      "background-color": "",
      "box-shadow": "",
      color: "",
    });
  }
});

// CSS CHANGES FOR BODY
// Need this for time changes for passages tagged "outside"
$(document).on(":passagerender", function (ev) {
  // Check if the current passage has the "outside" tag
  if (tags().includes("outside")) {
    // Check if the time is "Night"
    if (State.variables.time === "Night") {
      // Apply the night theme
      $("body").removeClass("evening").addClass("night");
    } else {
      // Otherwise, apply the evening theme
      $("body").removeClass("night").addClass("evening");
    }
  } else {
    // For passages without the "outside" tag, ensure the default theme
    $("body").removeClass("night").removeClass("evening");
  }
});

// GO TO START ON REFRESH
// window.onbeforeunload = function () {
//   window.sessionStorage.setItem("twine-reload-flag", "true");
// }; // Set the reload flag before the page unloads

// // Use the :passagedisplay event to check the flag and redirect if necessary
// $(document).on(":passagedisplay", function () {
//   var refresh = sessionStorage.getItem("twine-reload-flag");

//   // Clear the flag immediately after retrieving it to prevent unintended behavior
//   sessionStorage.removeItem("twine-reload-flag");

//   if (refresh === "true" && passage() !== "Start") {
//     // Ensure to only redirect if not on the 'Start' passage to avoid loops
//     Engine.play("Start"); // Replace 'somePassage' with your target passage
//   }
// });
