import 'dart:html';

main() async {
  var countdown = querySelector("#countdown");
  for (int i = 100; i >= 0; i--) {
    countdown.text = "Time: $i";
    await window.animationFrame;
  }
}
