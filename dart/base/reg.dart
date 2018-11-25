void main(){
  RegExp exp = new RegExp(r"(\w+)");
  String str = "Parse my string";
  Iterable<Match> matches = exp.allMatches(str);
  for (Match m in matches) {
  String match = m.group(0);
  print(match);
  }
}
