/*
------------------------------------------
File: asc_bin_toop_sort.cpp
Desc: Soring binary toops ascendingly
Author: Vladimir Kulyukin

To compile: g++ -o asc_bin_toop_sort asc_bin_toop_sort.cpp
To run: chmod u+x dsc_bin_toop_sort
        ./asc_bin_toop_sort < bin_toops.txt
        more bin_toops.txt | ./asc_bin_toop_sort
------------------------------------------
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct bin_toop { string key; long   val; };
bool asc_cmp_bin_toop(const bin_toop* bp1, const bin_toop* bp2) { return bp1->val < bp2->val; }

int main() {
  vector<bin_toop*> bin_toops;
  string key;
  long   val;
  bin_toop* bp;
  while ( cin >> key >> val ) {
    bp = new bin_toop();
    bp->key = key; bp->val = val;
    bin_toops.push_back(bp);
  }
  sort(bin_toops.begin(), bin_toops.end(), asc_cmp_bin_toop);
  for(vector<int>::size_type i = 0; i != bin_toops.size(); ++i) {
    cout << bin_toops[i]->key << "\t" << bin_toops[i]->val << endl;
  }
  return 0;
}
