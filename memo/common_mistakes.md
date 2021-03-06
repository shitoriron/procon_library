# Common mistakes

競プロでよくあるミスを挙げる．特に「なぜか通らない」時に見る．

## いいから黙って long long を使う．メモリがやばいとわかってから初めて int を使う.

##  問題文読み間違い

* 題意を読み間違えてるヤツ

## 入力の勘違い

* 特に入力の数を間違える．格納される値が少しずつずれる．

## 書き間違い

* 特にイテレータとして使う変数 i とか j の書き間違いはあるある 

## 出力のミス

* 特に答えが小数になる場合，cout はやめる．printf("%.3f\n", ans) とかにする．

## 問題タイプごとのミス

### 幾何

* 線分同士の交差と直線と線分の交差の違い．線分同士だと条件が増えることに注意．



## set で lower_bound  するときの注意

```
set<ll> st;
lower_bound(st.begin(), st.end(), key);
```

上のコードは実は O(N) かかってしまう．上記の lower_bound は，コンテナがランダムアクセス可能ならば O(logN) になるが，ランダムアクセスできない場合は O(N) になる．

set で O(logN) で lower_bound するためには

```
st.lower_bound(key);
```

とする．

## 1<<iと書かない，1ll<<i と書く
* 簡単にオーバーフローします

## メモ化再帰をするときに，初期値を安易に-1にしない
* もしもメモ化する値が負の値もとる場合，バグります

## if((j&mask)==0) と if((j&mask)==0) は違う
* ビット演算の結合順序はかなり意味不明なので注意

## 掛け算でオーバフロー
* にぶたんの時とか注意

## printf でllを表示するときに%lldを使う！

## 指数に関してmodを取る場合はmod-1で取らないとだめ！！
* CF round566 E
* a^(mod-1) = 1 (フェルマーの小定理) であることを思い出すとこうなります

## 巨大なメモリを確保するときはヒープ領域に！
* セグフォします https://ja.wikipedia.org/wiki/スタックオーバーフロー

## modと同時に別の値で割り算するときは混同しないように気をつける
* https://atcoder.jp/contests/abc135/tasks/abc135_d

## ロリハは2つ以上のmodでやろうとすると結構重くなる．2^64以外のmodなら以外と一つでも大丈夫→うそ，二個はないと衝突する
* https://atcoder.jp/contests/abc135/tasks/abc135_f

## DPでバグった時
* 場合分けがある時，何処かだけmax, min, modを忘れてないか？

## size_tとlong long とか int を比較するとき，負の数があるとバグることがある

## endlは遅いので\nを使った方がいい場合がある

## priority_queueを逆順で使う場合，演算子<ではなく>を定義する必要がある