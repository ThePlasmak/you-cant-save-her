// DESTROY THE UI BAR
UIBar.destroy();

// UNDO BUTTON
function updateUndoButton() {
  // Remove existing undo button if it exists
  $("#undobar").remove();

  // Add the undo button if $enable_undo is true
  if (State.variables.enable_undo) {
    $("body").prepend(
      "<div id='undobar'><a href='#' id='undoButton'>←</a></div>"
    );

    $("#undoButton").on("click", function (e) {
      e.preventDefault();
      Engine.backward();
    });
  }
}

// Run the update function on each passage render
$(document).on(":passagerender", function () {
  updateUndoButton();
});

// AUTOSAVE
$(document).on(":passagerender", function () {
  if (State.passage !== "Start") {
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
