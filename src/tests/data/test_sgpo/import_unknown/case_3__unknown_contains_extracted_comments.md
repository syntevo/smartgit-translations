In this test case, it is tested whether entries with extracted-comments are imported.
In BUILD: 21014, information to track where the unknown entry came from was added as an extracted-comment.
It is tested whether this can be imported correctly.

The extracted-comment is imported into the pot as is.
This specification is made with the anticipation that a process to manually delete the pot after checking and editing will be executed separately.

---
このテストケースではextracted-comment付きのエントリが取り込まれることをテストします。
BUILD: 21014 でunknownのentryがどこから来たのか追跡するための情報がextracted-commentとして付加されるようになりました。
これを正しくインポートできるかテストします。

pot には extracted-comment がそのまま取り込まれます。
この仕様は、potを確認編集したあとに手動で削除する工程を別で実行することを想定しています。