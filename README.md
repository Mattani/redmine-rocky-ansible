# redmine-rocky-ansible

最小構成でインストールしたRocky LinuxにRedmineを自動インストールするためのAnsibleプレイブックです。

コマンド5個実行するだけで、あとはしばらく放置すればインストールが完了します。

## 概要

Ansibleを使ってRedmineを自動インストールするためのプレイブックです。以下のwebサイトで紹介されている手順におおむね準拠しています。

[Redmine 3.4をCentOS 7.3にインストールする手順](http://blog.redmine.jp/articles/3_4/install/centos/)

ただし以下の点はMattaniが独自の修正をいれております

* OSはRocky Linux 8.9を使用します
* Rubyはrbenvによりインストールします
* Redmine/RedMicaをgitリポジトリから取得するように改変しています

## システム構成

* Redmine/RedMica
* Rocky Linux 8.9
* PostgreSQL
* Apache

## Redmineのインストール手順

インストール直後の Rocky Linux 8.9 に root でログインし以下の操作を行ってください。

### Ansibleとgitのインストール

```
dnf update -y
dnf install -y epel-release glibc-locale-source
dnf install -y ansible git
```

### playbookのダウンロード

```
git clone https://github.com/Mattani/redmine-rocky-ansible.git
```

### ダウンロードしたプレイブック内のファイル `group_vars/redmineserver` を編集

* Redmine/RedMicaの選択／バージョンの選択
  * `redmine_git_url` はRedmine/RedMicaどちらかを選択してください。（選択しないほうの `redmine_git_url` を `#`でコメントアウトしてください）
  * `redmine_version` はRedmine/RedMicaのリポジトリで定義されているタグ名をご使用ください
* PostgreSQLに設定するパスワードの変更
  * `db_passwd_redmine` を適当な内容に変更してください。これはPostgreSQLのRedmine用ユーザー redmine に設定されるパスワードです。

### playbook実行

下記コマンドを実行してください。Redmineの自動インストールが開始されます。

```
cd redmine-rocky-ansible
ansible-playbook -i hosts site.yml
```

10〜20分ほどでインストールが完了します。webブラウザで `http://サーバIPアドレス/redmine` にアクセスしてください。Redmineの画面が表示されるはずです。

## ライセンス

MIT License

## 作者

[ファーエンドテクノロジー株式会社](http://www.farend.co.jp/)

## 改変者

Mattani -- [Redmine.tokyo](https://redmine.tokyo/)/[Redmine Japan](https://redmine-japan.org/)スタッフ

このプレイブックはファーエンドテクノロジー株式会社作成の [`farend/redmine-centos-ansible`](https://github.com/farend/redmine-centos-ansible)  をベースに改変したものです

