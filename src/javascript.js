// DESTROY THE UI BAR
UIBar.destroy();

// SET UP THE OPTIONS
$(document).on(":start", function () {
  // UNDO BUTTON
  // Check if 'enableUndo' is stored in localStorage, set it to 'false' if not.
  if (localStorage.getItem("enableUndo") === null) {
    localStorage.setItem("enableUndo", "false"); // Set default to false if not present
  }

  // Load the enableUndo state from localStorage
  State.variables.enableUndo = localStorage.getItem("enableUndo") === "true";

  // Update the undo button based on the current state.
  updateUndoButton();

  // TIMED PAGE TRANSITIONS
  // Check if 'enableTimed' is stored in localStorage, set it to 'true' if not.
  if (localStorage.getItem("enableTimed") === null) {
    localStorage.setItem("enableTimed", "true"); // Set default to true if not present
  }

  // Load the enableTimed state from localStorage
  State.variables.enableTimed = localStorage.getItem("enableTimed") === "true";

  // LIGHT MODE
  // Check if 'enableLightMode' is stored in localStorage, set it to 'true' if not.
  if (localStorage.getItem("enableLightMode") === null) {
    localStorage.setItem("enableLightMode", "false"); // Set default to false if not present
  }

  // Load the enableLightMode state from localStorage
  State.variables.enableLightMode =
    localStorage.getItem("enableLightMode") === "true";
});

// UNDO BUTTON
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
  $("#undobar").remove(); // Remove existing undo button, if any.

  // If chapter selection is active, and if the current passage is one of the chapter starts, hide the undo button
  var isChapterSelectionActive = State.variables.chapter_select_active;
  var isChapterStartPassage = [
    "intro_1",
    "chapter_2",
    "chapter_3",
    "chapter_4",
    "chapter_5",
  ].includes(State.passage);

  var isChapterNoUndo = isChapterSelectionActive && isChapterStartPassage;

  if (setup.enableUndo.get() && !isChapterNoUndo) {
    // Show the undo button only if undo is enabled and not in the first page after chapter selection mode
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

// TIMED PAGE TRANSITIONS OPTION
setup.enableTimed = {
  // Retrieves the current enableTimed state from localStorage, defaulting to true
  get: function () {
    return localStorage.getItem("enableTimed") === "true";
  },

  // Toggles the enableTimed state and saves the new state to localStorage
  toggle: function () {
    var currentState = this.get();
    localStorage.setItem("enableTimed", !currentState);
    State.variables.enableTimed = !currentState;

    // Refresh the current passage to reflect the change immediately
    Engine.play(passage());
  },
};

// Initialize the enableTimed state on document ready
$(document).ready(function () {
  if (localStorage.getItem("enableTimed") === null) {
    localStorage.setItem("enableTimed", "true");
  }
  State.variables.enableTimed = localStorage.getItem("enableTimed") === "true";
});

// LIGHT MODE OPTION
setup.enableLightMode = {
  // Retrieves the current state from localStorage, defaulting to false
  get: function () {
    return localStorage.getItem("enableLightMode") === "true";
  },

  // Toggles the state and saves the new state to localStorage
  toggle: function () {
    var currentState = this.get();
    localStorage.setItem("enableLightMode", !currentState);
    State.variables.enableLightMode = !currentState;

    // Refresh the current passage to reflect the change immediately
    Engine.play(passage());
  },
};

// Change the CSS if light mode is active
$(document).on(":passagerender", function (ev) {
  if (setup.enableLightMode.get()) {
    document.documentElement.setAttribute("data-theme", "light");
    localStorage.setItem("theme", "light");
  } else {
    document.documentElement.setAttribute("data-theme", "dark");
    localStorage.setItem("theme", "dark");
  }
});

// AUTOSAVE
// Autosaves whenever you enter a new passage
$(document).on(":passagerender", function () {
  // Check if that passage allows autosaving
  if (
    State.variables.chapter_select_active !== true &&
    ![
      "Start",
      "options",
      "content_warning",
      "content_warning_restart",
      "headphones",
      "headphones_restart",
      "its_okay",
      "credits",
      "chapters",
      "restart",
      "about",
      "lines",
    ].includes(State.passage)
  ) {
    Save.slots.save(1); // Automatically save to slot 1
  }
});

// SCROLL TO TOP OF WINDOW ON PASSAGE RENDER
$(document).on(":passagerender", function () {
  window.scrollTo(0, 0);
});

// CHECK AUDIO
// Check to see if trackID is the currently playing track
window.isPlaying = function (trackID) {
  var track = SimpleAudio.tracks.get(trackID);
  return track !== null && track.isPlaying();
};

// GO TO START ON REFRESH
window.onbeforeunload = function () {
  window.sessionStorage.setItem("twine-reload-flag", "true");
}; // Set the reload flag before the page unloads

// Use the :passagedisplay event to check the flag and redirect if necessary
$(document).on(":passagedisplay", function () {
  var refresh = sessionStorage.getItem("twine-reload-flag");

  // Clear the flag immediately after retrieving it to prevent unintended behavior
  sessionStorage.removeItem("twine-reload-flag");

  if (refresh === "true" && passage() !== "Start") {
    // Ensure to only redirect if not on the 'Start' passage to avoid loops
    Engine.play("Start");
  }
});
