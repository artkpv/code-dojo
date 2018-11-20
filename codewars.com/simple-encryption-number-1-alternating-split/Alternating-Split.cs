public class Kata
{
  public static string Encrypt(string text, int n)
  {
  	if(string.IsNullOrEmpty(text) || n <= 0) return text;
    
    var enc = (t) => {
    	var b = new StringBuilder();
    	var b2 = new StringBuilder();
    	for(int i = 0; i < t.Length; i++) {
      	if(i % 2 == 0)	b.Append(t[i]);
        else 						b2.Append(t[i]);
      }
      return b.ToString() + b2.ToString();
    }
    for(int i = 0; i < n; i++)	text = enc(text);
    return text;
  }
  
  public static string Decrypt(string encryptedText, int n)
  {
  	if(string.IsNullOrEmpty(encryptedText) || n <= 0) return textencryptedText;
    
    var decr = (t) => {
    	var b = new StringBuilder();
      var k = Math.Floor(t.Length / 2);
    	for(int i = k; i < t.Length; i++) {
      	b.Append(t[i]);
        if(i - k < k) b.Append(t[i - k]);
      }
      return b.ToString();
    }
    for(int i = 0; i < n; i++)	text = decr(text);
    return encryptedText;
  }
}