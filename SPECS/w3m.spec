%define	man_ja	ja
Summary: A Pager with WWW capability (UTF-8, CJK enhanced)
Summary(ja): World Wide Web に対応したページャ (UTF-8, CJK 拡張)
Name: w3m
Version: 0.5.1
Release: 1
Group: Applications/Internet
Copyright: Freely distributable
# w3m original URL
# Url: http://ei5nazha.yz.yamagata-u.ac.jp/
URL: http://w3m.sourceforge.net/
# Source0: ftp://ei5nazha.yz.yamagata-u.ac.jp/w3m/w3m-%{version}.tar.gz
Source0: http://prdownloads.sourceforge.net/w3m/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: gc openssl perl
Provides: webclient w3m
BuildPrereq: ncurses-devel gc-devel openssl-devel

Vendor: masao (derived from Project Vine)
Distribution: masao (derived from Vine Linux)

%description
w3m is a pager with WWW capability. It IS a pager, but it can be
used as a text-mode WWW browser. The features of w3m are as follows:
- When reading HTML document, you can follow links and view images
  (using external image viewer).
- It has 'internet message mode', which determines the type of document
  from header. If the Content-Type: field of the document is text/html,
  that document is displayed as HTML document.
- You can change URL description like 'http://hogege.net' in plain text
  into link to that URL.

%description -l ja
w3m は，ページャfmをベースに開発された World Wide Web に対応したページャ
です．fm の機能に加えて、w3m の特徴には，次のようなものがあります．
・WWW 対応なので，HTML の文書を読んでいる時には，その中のリンクを辿った
  り，画像を見ることができる．
・Internet message 表示のためのモードがある．この時，Content-Type: が
  text/html の場合は，自動的に HTML の文書として表示する．また，自力で
 MIME header のデコードをする．
・見ている plain text 文書中に URL 表記があった場合，その部分からリンク
  をたどることができる．


%prep
%setup -q


%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --disable-image --enable-japanese=E
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}

# prepare applnk

%define applnkdir /etc/X11/applnk/Internet
mkdir -p $RPM_BUILD_ROOT/%{applnkdir}
cat > $RPM_BUILD_ROOT/%{applnkdir}/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Type=Application
Comment=A Pager with WWW capability
Comment[ja]=WWW対応ページャ
Exec=kterm -e %{name}
Terminal=false
EOF

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc doc doc-jp
%config(missingok) %{applnkdir}/%{name}.desktop
%{_bindir}/w3m
%{_bindir}/w3mman
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/%{man_ja}/man1/w3m*
%{_mandir}/man1/w3m*
%{_datadir}/locale/*/LC_MESSAGES/w3m.mo


%changelog
* Thu Feb  3 2005 Masao Takaku <masao@nii.ac.jp> 0.5.1-masao1
- update to w3m-0.5.1 (m17n package was integrated...)

* Thu Jul 19 2001 Shoji Matsumoto <shom@vinelinux.org> 0.19-0vl1
- update to 0.19 (based on w3m-0.2.1)

* Mon Mar 26 2001 Shoji Matsumoto <shom@vinelinux.org> 0.17-0vl1
- update to 0.17 (based on w3m-0.2.1)

* Tue Mar  6 2001 Shoji Matsumoto <shom@vinelinux.org> 0.13-0vl1
- created (based on w3m-0.1.10-0vl6)

* Wed Dec 20 2000 MATSUBAYASHI 'Shaolin' Kohji <shaolin@rhythmaning.org>
- 0.1.10-0vl6
- use better macros
- rebuilt with ncurses5

* Thu Sep 21 2000 Jun Nishii <jun@vinelinux.org>
- w3m-0.1.10-0vl5
- use applnk instead of wmconfig
- use openssl

* Thu Jul 27 2000 Lisa Sagami <czs14350@mb.infoweb.ne.jp>
- w3m-0.1.10-0vl4
- fix typo in w3m.csh and w3m.wmconfig

* Sun Jul 09 2000 Lisa Sagami <czs14350@nifty.ne.jp>
- w3m-0.1.10-0vl3
- provide default HTTP_HOME in /etc/profile.d

* Fri Jul 07 2000 Lisa Sagami <czs14350@nifty.ne.jp>
- Provides: webclient, Requires: indexhtml (capability of lynx)
- added w3m.wmconfig
- give them(who?) RPM_OPT_FLAGS(what?)
- dont include duplicated man pages and CVS directory in doc

* Wed Jun 21 2000 Jun Nishii <jun@vinelinux.org>
- 0.1.10-0vl1

* Sat Jan 22 2000 Yoichi Imai <yoichi@silver-forest.com>
- fix spec file

* Sat Jan 22 2000 Yoichi Imai <yoichi@silver-forest.com>
- updated from 0.1.4 to 0.1.6

* Thu Jan 13 2000 Yoichi Imai <yoichi@silver-forest.com>
- updated from 991203 to 0.1.4

* Fri Dec 03 1999 Yoichi Imai <yoichi@silver-forest.com>
- updated from 991028 to 991203

* Sat Oct 30 1999 Yoichi Imai <bonaim@mutt.freemail.ne.jp>
- updated from 990820 to 991028

* Tue Aug 26 1999 Ryo Hattori <ryoh@vs01.vaio.ne.jp>
- updated from 990716 to 990820

* Wed Aug 11 1999 Ryo Hattori <ryoh@vs01.vaio.ne.jp>
- initial Release to VinePlus
