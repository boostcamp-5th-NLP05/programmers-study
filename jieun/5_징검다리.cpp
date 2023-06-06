#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX 200000

vector<int> rightg(MAX + 2);
vector<int> leftg(MAX + 2);

int find_left(int x)
{
    if (leftg[x] == x)
        return x;
    return leftg[x] = find_left(leftg[x]);
}

int find_right(int x)
{
    if (rightg[x] == x)
        return x;
    return rightg[x] = find_right(rightg[x]);
}

void union_left(int x, int y)
{
    x = find_left(x);
    y = find_left(y);
    if (x < y)
        leftg[y] = x;
    else
        leftg[x] = y;
}

void union_right(int x, int y)
{
    x = find_right(x);
    y = find_right(y);
    if (x > y)
        rightg[y] = x;
    else
        rightg[x] = y;
}

int solution(vector<int> stones, int k)
{
    int answer = 0;
    int N = stones.size();

    vector<pair<int, int>> values(N);
    for (int i = 0; i < N; i++)
    {
        values[i] = make_pair(stones[i], i + 1);
    }
    sort(values.begin(), values.end());

    for (int i = 0; i < N + 2; i++)
    {
        rightg[i] = i;
        leftg[i] = i;
    }

    int last_cnt = 0;
    for (int i = 0; i < values.size(); i++)
    {
        int cur_val = values[i].first;
        int cur_idx = values[i].second;
        last_cnt = max(last_cnt, cur_val);
        union_left(cur_idx, cur_idx - 1);
        union_right(cur_idx, cur_idx + 1);
        if (find_right(cur_idx) - find_left(cur_idx) > k)
            break;
    }

    answer = last_cnt;

    return answer;
}