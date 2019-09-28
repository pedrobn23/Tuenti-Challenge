#include<iostream>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

typedef char byte;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)


int mapamundi256( int a, int b)
{
  return (a-b) + ((a-b)<0 ? 256 : 0);
}

vector<byte> notSoComplexHash(const string &inputText) {
  vector<char> hash = vector<char>(16, 0x00);
  int j=0;
  for (int i = 0; i < inputText.length(); i++) {
    if (inputText[i] != '\r' && inputText[i] != '\n') {
      hash[j % 16] = (hash[j % 16] + inputText[i]);
      j++;
    }
  }
  return hash;
}


void print_vec(vector<char> v)
{
  for( auto a : v)
    cout << int(a)<< " ";
  cout << endl;
}

bool equal_vec(const vector<byte>& ori, const vector<byte>& mod,
               const vector<int> &n_ceros)
{
  for( int i = 0; i < mod.size(); ++i )
    {
      int num = ori[i]-mod[i];
      int num2= mapamundi256(ori[i],mod[i]);
      cout << num << ":"<< num2 << ":" << n_ceros[i] << endl;

      if( !((num2 <=74*n_ceros[i]) ) )
        return false;
    }
  return true;
}


int distancia(string original, string altered)
{
  string mod = altered;
  int first = altered.find_first_of('-');
  auto s1 = altered.substr(0, first);
  auto s2 = altered.substr(first+6, string::npos);
  cout << "first: " << first << endl;

  int first0 = first+3;
  vector<int> n_ceros(16,0);


  string hack;
  vector<byte> althash = notSoComplexHash(altered);
  vector<byte> orihash = notSoComplexHash(original);
  vector<byte> modhash = notSoComplexHash(s1+hack+s2);
  int i = 0;

  cout << s1<< endl;
  while(!(equal_vec(orihash,modhash,n_ceros)))
    {
      n_ceros[first0%16]+=1;
      cout << endl << n_ceros[first0%16] << endl;
      first0+=1;
      hack += '0';
      cout << hack << endl;
      cout << hack.length()<< endl;
      modhash=notSoComplexHash(s1+hack+s2);
      i += 1;
    }

  cout << i;


  return 0;
}

void Problema7( string original, string altered )
{
  int dist = distancia(original, altered);
}


int main()
{
  string original, altered, aux, trash;
  int M, T;
  cin >> T;

  FOR(i,0,T) {
    stringstream ss, ss2;

    cin >> M;
    getline(cin, trash);
    FOR (j,0, M) {
      getline(cin, aux);
      ss << aux;
    }
    original = ss.str();

    cout << original << endl << endl;

    cin >> M;
    getline(cin, trash);
    FOR (j,0, M) {
      getline(cin, aux);
      ss2 << aux;
    }
    altered = ss2.str();

    cout << altered << endl << endl;

    cout << "Case #" << i+1 << ": " ;
    Problema7(original, altered);
  }
}
