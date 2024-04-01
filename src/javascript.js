UIBar.destroy();

// TODO: Implement this undo button later
// $("body").prepend(
//   "<div id='undobar'><a href='javascript:void(0)' onclick='Engine.backward()'>←</a></div>"
// );

$(document).one(":passagerender", function () {
  $("body").prepend(
    "<div id='undobar'><a href='#' id='undoButton'>←</a></div>"
  );

  $("#undoButton").on("click", function (e) {
    e.preventDefault();
    Engine.backward();
  });
});
