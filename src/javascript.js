// DESTROY THE UI BAR
UIBar.destroy();

// UNDO BUTTON
// Simplify the initial check and setting of the enableUndo variable
$(document).on(":start", function () {
  // Correctly set State variable based on localStorage, with a fallback to true if not set
  State.variables.enableUndo =
    localStorage.getItem("enableUndo") !== null
      ? localStorage.getItem("enableUndo") === "true"
      : true;
});

setup.enableUndo = {
  // Retrieves the current undo state from localStorage, correctly handling "true" and "false" strings
  get: function () {
    var value = localStorage.getItem("enableUndo");
    return value === "true"; // Correctly returns false if value is "false"
  },

  // Toggles the undo state and saves the new state to localStorage
  toggle: function () {
    var currentState = this.get();
    localStorage.setItem("enableUndo", !currentState);

    // Ensure the state variable is also updated
    State.variables.enableUndo = !currentState;

    // Optionally, refresh the current passage to reflect the change immediately
    Engine.play(passage());
  },
};

function updateUndoButton() {
  $("#undobar").remove(); // Remove existing Undo button, if any.

  if (setup.enableUndo.get()) {
    // Use the setup object's method for consistency.
    $("body").prepend(
      "<div id='undobar'><a href='#' id='undoButton'>←</a></div>"
    );

    $("#undoButton").on("click", function (e) {
      e.preventDefault();
      Engine.backward();
    });
  }
}

// Initialize the undo button based on the current state
$(document).on(":passagerender", updateUndoButton);

// AUTOSAVE
$(document).on(":passagerender", function () {
  // Check if the current passage is neither "Start" nor "options"
  if (State.passage !== "Start" && State.passage !== "options") {
    Save.slots.save(1); // Automatically save to slot 1
  }
});

// CSS CHANGES
$(document).on(":passagerender", function (ev) {
  // Get the current passage's tags
  var currentTags = tags();

  // Check if the "letter" tag is included
  if (currentTags.includes("letter")) {
    // Apply styles for passages with the "letter" tag
    $("#passages").css({
      "background-color": "transparent",
      "box-shadow": "none",
    });
  } else {
    // Reset styles for passages without certain tags
    $("#passages").css({
      "background-color": "",
      "box-shadow": "",
    });
  }
});

// GO TO START ON REFRESH
window.onbeforeunload = function () {
  window.sessionStorage.setItem("twine-reload-flag", "true");
};

postdisplay["refresh-taker"] = function (t) {
  delete postdisplay[t];
  var refresh = sessionStorage.getItem("twine-reload-flag");

  if (refresh === "true" && passage() !== "Start") {
    // your starting passage here

    Engine.play("Start"); // passage to forward player to
  }
};
