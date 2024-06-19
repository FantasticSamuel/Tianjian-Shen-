#include<bits/stdc++.h>
//author 沈天健 2300011417 
using namespace std;
string s;
int main()
{
	while(cin>>s)
    {
        int l=s.length();
		if(s[0]!="."&&s[0]!="@"&&s[l-1]!="."&&s[l-1]!="@")
	    {
	        int i=s.find("@");
	        if(s.find(".",i)!=string::npos&&s.find("@",i)==string::npos&&s.find(".@")==string::npos&&s.find("@.")==string::npos)
	        {
	                cout<<"YES"<<endl;
	                continue;
	        }
	    }
	    cout<<"NO"<<endl;
	}
}