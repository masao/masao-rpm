%define nam	wget
%define ver	1.8.2
%define rel	3
%define __serial	2002121601
%define __libtoolize echo

Summary: A utility for retrieving files using the HTTP or FTP protocols.
Summary(zh_CN): [通讯]功能强大的下载程序,支持断点续传
Summary(zh_TW.Big5): [伋侎伆佋]仴佨挴鄟眮陙陹仱佌捀鼇祦麙,挙鋻伮佭伮伾捘驋肚
Name: %{nam}
Version: %{ver}
Release: %{rel}
Group: Applications/File
License: GPL

Source0: ftp://ftp.gnu.org/gnu/wget/wget-%{ver}.tar.gz
Patch1: wget-1.7-zh_CN-ko-po.patch
Patch2:	wget-1.8.2-filename.patch
Serial: %{__serial}
Buildroot: /var/tmp/%{name}-%{version}-root
Provides: webclient
Prereq: /sbin/install-info
Requires: openssl
BuildRequires: openssl-devel
Prefix: /etc
#NoSource: 0


%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols.  Wget features include the ability to work in the
background while you're logged out, recursive retrieval of directories,
file name wildcard matching, remote file timestamp storage and comparison,
use of Rest with FTP servers and Range with HTTP servers to retrieve files
over slow or unstable connections, support for Proxy servers, and
configurability.

Install wget if you need to retrieve large numbers of files with HTTP or
FTP, or if you need a utility for mirroring web sites or FTP directories.

%changelog
* Mon Dec 16 2002 Masaru Yokoi <masaru@turbolinux.co.jp>
- 1.8.2-3
- Security: wget-1.8.2-filename.patch to fix ftp path problem.

* Thu May 30 2002 Merlin Ma <merlin@turbolinux.com.cn>
- updated to 1.8.2

* Wed Feb 27 2002 Kiichiro NAKA <knaka@turbolinux.co.jp>
- 1.8.1-2
- enabled ssl support

* Mon Jan 7 2002 Masaru Yokoi <masaru@turbolinux.co.jp>
- upgraded to version 1.8.1.

* Wed Jul 4 2001 James Su <suzhe@turbolinux.com.cn>
- fixed the wrong charsets in zh_CN.po and kr.po

* Wed Jun 6 2001 Hirofumi Takeda <takepin@turbolinux.co.jp>
- updated to 1.7

* Tue May 08 2001 Masaru Yokoi <masaru@turbolinux.co.jp>
- Added wget-1.6-zh_TW.po-skip.patch to remove illegal chars in glibc-2.2.

* Thu Mar 27 2001 Joe Li <joe.li@turbolinux.com.cn>
- Changed zh.po into zh_TW.po
- added zh_CN.po and ko.po.

* Thu Jan 04 2001 Masaru Yokoi <masaru@turbolinux.co.jp>
- Updated to version 1.6.
- Removed IPv6 patch tempolary.

* Fri Sep 22 2000 Masaru Yokoi <masaru@turbolinux.co.jp>
- Added IPv6 patch.

* Thu Aug 10 2000 SL Baur  <steve@turbolinux.co.jp>
- This spec file has been changed anonymously at least twice since June.
- fix for rpm-4, fix for non-intel

* Mon Oct 25 1999 Kelley Spoon <kspoon@turbolinux.com>
- moved info dir to /usr/share/info

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree
- add Provides

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.5.3

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.5.2

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- modified group to Applications/Networking

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.0
- they removed the man page from the distribution (Duh!) and I added it back
  from 1.4.5. Hey, removing the man page is DUMB!

* Fri Nov 14 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc

#--------------------------------------------------
%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch1 -p1
%patch2 -p1
%build
%configure --enable-ipv6 --with-ssl
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
gzip $RPM_BUILD_ROOT%{_infodir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/wgetrc
%{_mandir}/man1/wget.1*
%{_bindir}/wget
%{_infodir}/*
%{_datadir}/locale/*/LC_MESSAGES/wget.mo
%doc AUTHORS COPYING ChangeLog MAILING-LIST NEWS PATCHES README TODO

%post
/sbin/install-info %{_infodir}/wget.info.gz %{_datadir}/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_datadir}/wget.info.gz %{_datadir}/dir
fi


