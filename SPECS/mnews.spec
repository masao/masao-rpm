Summary: mnews - mini news reader
Summary(ja): mnews - ミニ・ニュースリーダ
Name: mnews
Version: 1.22PL7
Release: 5m
Group: Applications/Networking
License: distributable
Source0: %{name}122PL7.tar.gz 
Patch0: %{name}-1.22-ignore.patch 
Patch1: %{name}-1.22PL1-vine.patch 
# Patch2: %{name}-alpha.diff
Patch3: %{name}-unexpandtab.patch
Patch4: %{name}-1.22PL7-rfc2822.patch
Patch5: %{name}-line.patch
Patch6: %{name}-compat-castptr.patch
Patch7: %{name}1.22PL7-unicode-20080202.patch
Patch8: %{name}-unicode-fix.patch
Patch9: %{name}-unicode-fix2.patch
Patch10: %{name}-unicode-dash.patch
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Masao Takaku
Distribution: Derived from Vine Linux

%description
mnews is mini news/mail reader.

%description -l ja
mnews は電子ニュース/電子メールを読むための小型のニュースリーダです。
mnews は小型化、高速化、そして簡単に使用できることを目標に開発されました。

%prep
%setup
%patch0 -b .ignore
%patch1 -b .vine
# %patch2 -p1 -b .alpha
%patch3 -b .unexpandtab
%patch4 -b .rfc2822
%patch5 -b .line
%patch6 -b .castptr
%patch7 -p1 -b .unicode
%patch8 -b .ufix
%patch9 -b .ufix2
%patch10 -b .dash

%build
cd build
./config.sh << EOF

7
y

%{_bindir}
%{_libdir}/mnews
%{_mandir}
/tmp
y
y
y
y
y
y
/var/spool/news
/var/lib/news
/var/spool/mail
y
/usr/bin/inews -h
y
/usr/sbin/sendmail -t -om -oi
y
y
y
y
y
y
y
/var/spool/board
y
animate
display
display
play
gv
y
/usr/bin/less
y
n
n
n
-DCTRL_L -DCOMPLETION -DREF_SORT -DLARGE -DDISPLAY_CTRL -DINET6 -DBUILTIN_MMH -DCOLOR -DNNTP_AUTH -DSUPPORT_X0201 -DTRI -DUSE_NLINK -DXOVER -DUNICODE
domain.name
5
5
1
5
5
1
1
1
mnewsprint
y
n
n
y
n
y
y
y
/usr/bin/gcc
%{optflags} -DUSE_TERMIOS
/usr/bin/emacs
y
EOF
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/mnews
mkdir -p %{buildroot}%{_mandir}/ja/man1

cd build
make DESTDIR=%{buildroot} install

#( cd %{buildroot}
#  gzip -9nf .%{prefix}/man/ja/man*/*
#)

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc doc/*.doc etc/jnames.* etc/_mnews.smp
%{_bindir}/mnews
%{_mandir}/ja/man1/mnews.1*
%dir %{_libdir}/mnews
%config %{_libdir}/mnews/default-domain

%changelog
* Mon May 20 2013 <masao@slis.tsukuba.ac.jp>
- 1.22PL7-m3
- add a patch for utf-8 supports.

* Wed Jun 01 2005 <masao@nii.ac.jp>
- 1.22PL7-m2:
- add a patch for correct line number.

* Wed Feb 02 2005 <masao@nii.ac.jp>
- 1.22PL7-m1:
- updated to 1.22PL7 release.
- add mnews-unexpandtab.diff

* Sat Jun 09 2001 <sagami@vinelinux.org>
- 1.22PL1-1vl4: minor spec fixes

* Fri May 25 2001 Tomoya TAKA <tomoya@olive.plala.or.jp>
- 1.22PL1-1vl3
- add mnews-alpha.diff taken from Kondara MNU/Linux
- use macros

* Fri Sep 08 2000 MATSUBAYASHI 'Shaolin' Kohji <shaolin@rhythmaning.org>
- 1.22PL1-1vl2
- ja_JP.ujis -> ja (including modification of vine patch)

* Fri Mar 3 2000 Taro FUNAKI <taro@KU3G.org>
- updated to 1.22PL1

* Fri Dec 24 1999 Taro FUNAKI <taro@KU3G.org>
- updated to 1.22
