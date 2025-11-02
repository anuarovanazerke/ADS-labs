 //A
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;

vector<string> v;
unordered_set<string> st;

string hashing(const string &s) {
    ll h = 0, p = 1;
    for (char c : s) {
        h = (h + ((c - 47) * p) % mod) % mod;
        p = (p * 11) % mod;
    }
    return to_string(h);
}
void solve(){
    dalshe menshe

    int n; string s;

    cin >> n;
    for(int i = 1; i <= n * 2; i++){
        cin >> s;
        v.push_back(s);
        st.insert(s);
    }

    int cnt = 0;

    for(int i = 0; i < v.size(); i++){
        if(cnt == n) break;
        string hs = hashing(v[i]);
        if(st.find(hs) != st.end()){
            cout << "Hash of string \"" << v[i] << "\"" << " is " << hs << endl;
            cnt++;
        }
    }
}

signed main() {

    dalshe menshe

    int tt = 1;
    while(tt--){

        solve();

    }
    return 0;
}


//B
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;
const ll pw = 31;

vector<long long> prefix_hash(string s) {
    int n = s.size();
    vector<long long> h(n + 5, 0), p(n + 5, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return h;
}

ll get_hash(const vector<ll> &h, const vector<ll> &p, int l, int r) {
    ll res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}

void solve(){

    string s1, s2, t;
    cin >> s1 >> s2 >> t;

    int n = s1.size(), m = t.size();

    auto h1 = prefix_hash(s1);
    auto h2 = prefix_hash(s2);
    vector<long long> p(n + 1, 1);
    for (int i = 1; i <= n; i++) p[i] = (p[i - 1] * pw) % mod;

    long long hash_t = 0;
    for (char c : t) hash_t = (hash_t * pw + (c - 'a' + 1)) % mod;

    int count = 0;
    for (int i = 0; i + m <= n; i++) {
        long long h_s1 = get_hash(h1, p, i, i + m);
        long long h_s2 = get_hash(h2, p, i, i + m);
        if (h_s1 == hash_t && h_s2 == hash_t) count++;
    }

    cout << count;

}

signed main() {

    int tt = 1;
    while(tt--){

        solve();

    }
    return 0;
}

//C
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;
const ll pw = 31;

vector<long long> prefix_hash(string s) {
    int n = s.size();
    vector<long long> h(n + 5, 0), p(n + 5, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return h;
}

ll get_hash(const vector<ll> &h, const vector<ll> &p, int l, int r) {
    ll res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}

void solve(){
    string s, t, check;
    int n;

    cin >> s;

    for(int i = 0; i < s.size(); i++) check += '0';

    auto h = prefix_hash(s);
    vector<long long> p(s.size() + 1, 1);
    for (int i = 1; i <= s.size(); i++) p[i] = (p[i - 1] * pw) % mod;

    cin >> n;

    for(int i = 1;i <= n; i++){
        cin >> t;
        long long hash_t = 0;
        for (char c : t) hash_t = (hash_t * pw + (c - 'a' + 1)) % mod;
        for(int j = 0; j + t.size() <= s.size(); j++){
            long long substr_hash = get_hash(h, p, j, j + t.size());
            if(substr_hash == hash_t)
                for(int k = j; k < j + t.size(); k++) check[k] = '1';
        }
    }
    for(int i = 0; i < check.size(); i++){
        if(check[i] == '0'){
            cout << "NO";
            return;
        }
    }
    cout << "YES";
}


signed main() {
    int tt = 1;
    while(tt--){

        solve();

    }

    return 0;
}

//D
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;
const ll pw = 31;

vector<long long> prefix_hash(string s) {
    int n = s.size();
    vector<long long> h(n + 5, 0), p(n + 5, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return h;
}
ll get_hash(const vector<ll> &h, const vector<ll> &p, int l, int r) {
    ll res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}
string s[155], long_str;
ll mx, str_cnt[155];

void solve(int n){

    mx = INT_MIN;

    for(int i = 1; i <= n; i++) cin >> s[i];

    cin >> long_str;

    auto h = prefix_hash(long_str);

    vector<long long> p(long_str.size() + 1, 1);

    for (int i = 1; i <= long_str.size(); i++) p[i] = (p[i - 1] * pw) % mod;

    for(int i = 1; i <= n; i++){
        long long hash_s = 0, cnt = 0;
        for(char c : s[i]) hash_s = (hash_s * pw + (c - 'a' + 1)) % mod;
        for(int j = 0; j + s[i].size() <= long_str.size(); j++){
            long long substr_hash = get_hash(h, p, j, j + s[i].size());
            if(substr_hash == hash_s) cnt++;
        }
        mx = max(mx, cnt);
        str_cnt[i] = cnt;
    }
    cout << mx << '\n';
    for(int i = 1; i <= n; i++){
        if(str_cnt[i] == mx) cout << s[i] << '\n';
    }
}


signed main() {
    int tt = 1;
    while(true){

        cin >> tt;

        if(tt == 0) break;
        else solve(tt);

    }

    return 0;
}

//E
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;
const ll pw = 31;

vector<long long> prefix_hash(string s) {
    int n = s.size();
    vector<long long> h(n + 5, 0), p(n + 5, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return h;
}

ll get_hash(const vector<ll> &h, const vector<ll> &p, int l, int r) {
    ll res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}

ll n, h[55], power[55], a[55];
string ans;

void solve(){
    cin >> n;

    power[0] = 1;

    for(int i = 1; i <= 51; i++){
        power[i] = power[i-1] * 2;
    }

    for(int i = 0; i < n; i++) {
        cin >> a[i];
        ll cur;
        if(i > 0) cur = (a[i] - a[i-1]) / power[i] + 97;
        else cur = a[i] + 97;
        cout << char(cur);
    }

}


signed main() {
    int tt = 1;
    while(tt--){

        solve();

    }

    return 0;
}

//F
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod1 = 1e9 + 7;
const ll mod2 = 1e9 + 9;
const ll pw1 = 31;
const ll pw2 = 37;

vector<ll> h1(2002, 0), h2(2002, 0);
vector<ll> p1(2002, 1), p2(2002, 1);

pair<ll, ll> get_hash(int l, int r) {
    pair<ll, ll> res = {(h1[r] - h1[l] * p1[r - l]) % mod1, (h2[r] - h2[l] * p2[r - l]) % mod2};
    if (res.first < 0) res.first += mod1;
    if (res.second < 0) res.second += mod2;
    return res;
}

void solve(){

    string s;
    unordered_set<uint64_t> st;

    cin >> s;

    int n = s.size();

    for (int i = 0; i < n; i++) {
        h1[i + 1] = (h1[i] * pw1 + (s[i] - 'a' + 1)) % mod1;
        h2[i + 1] = (h2[i] * pw2 + (s[i] - 'a' + 1)) % mod2;
    }

    for(int i = 1; i <= s.size(); i++){
        for(int j = 0; j + i <= s.size(); j++){
            pair<ll, ll> p = get_hash(j, j + i);
            uint64_t combine = ((uint64_t)p.F << 32) | ((uint64_t)p.S);
            st.insert(combine);
        }
    }
    cout << st.size();
}


signed main() {
    int tt = 1;
    for (int i = 1; i < 2002; i++) {
        p1[i] = (p1[i-1] * pw1) % mod1;
        p2[i] = (p2[i-1] * pw2) % mod2;
    }

    while(tt--){

        solve();

    }
    return 0;
}

//G
#include <bits/stdc++.h>
#define dalshe ios_base::sync_with_stdio(false);
#define menshe cin.tie(NULL);cout.tie(NULL);
#define all(x) x.begin(), x.end()
#define pii pair<int,int>
#define F first
#define ll long long
#define ld long double
#define S second
//#define mp make_pair
#define pb push_back
#define in insert
#define endl '\n'

using namespace std;

const ll N = 2e5 + 17;
const ll inf = 1e9 + 7;
const ll mod = 1e9 + 7;
const ll pw = 37;

const ll mod1 = 1000000007;
const ll mod2 = 1000000009;
const ll pw1 = 31;
const ll pw2 = 37;

pair<vector<ll>, vector<ll>> prefix_hash(const string &s, ll mod, ll pw) {
    int n = s.size();
    vector<ll> h(n + 1, 0), p(n + 1, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return {h, p};
}

ll get_hash(const vector<ll> &h, const vector<ll> &p, int l, int r, ll mod) {
    ll res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}

ll hashify(string tmp){
    long long hash_tmp = 0;
    for(char c : tmp) hash_tmp = (hash_tmp * pw + (c - 'a' + 1)) % mod;
    return hash_tmp;
}

string s;
int n, l, r;
unordered_map<uint64_t, int> mp;

void solve(){
    cin >> s >> n;

    auto [h1, p1] = prefix_hash(s, mod1, pw1);
    auto [h2, p2] = prefix_hash(s, mod2, pw2);

    for(int i = 0; i < s.size(); i++){
        for(int j = i + 1; j <= s.size(); j++){
            ll x1 = get_hash(h1, p1, i, j, mod1);
            ll x2 = get_hash(h2, p2, i, j, mod2);
            uint64_t key = ((uint64_t)x1 << 32) ^ (uint64_t)x2;
            mp[key]++;
        }
    }

    for(int i = 1; i <= n; i++){
        cin >> l >> r;
        l--;
        ll x1 = get_hash(h1, p1, l, r, mod1);
        ll x2 = get_hash(h2, p2, l, r, mod2);

        uint64_t combine = (((uint64_t)x1 << 32) ^ (uint64_t)x2);
        cout << mp[combine] << '\n';
    }
}


signed main() {
    int tt = 1;
    while(tt--){

        solve();

    }
    return 0;
}