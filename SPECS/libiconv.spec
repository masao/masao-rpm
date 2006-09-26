%define distrib Turbolinux
%define name	libiconv
%define	ver	1.11
%define rel	masao1
%define	prefix	/usr

Summary: libiconv - character set conversion library
Name: %{name}
Version: %{ver}
Release: %{rel}
Group: Development/Libraries
License: LGPL
URL:     http://www.gnu.org/software/libiconv/
Source:  ftp://ftp.gnu.org/pub/gnu/libiconv/%{name}-%{version}.tar.gz
Serial: 20060926
Distribution: %{distrib}
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
libiconv library provides an iconv() implementation, for use on
systems which don't have one, or whose implementation cannot convert
from/to Unicode.

libiconv provides support for the encodings:
European languages
  ASCII, ISO-8859-{1,2,3,4,5,7,9,10,13,14,15,16},
  KOI8-R, KOI8-U, KOI8-RU,
  CP{1250,1251,1252,1253,1254,1257}, CP{850,866},
  Mac{Roman,CentralEurope,Iceland,Croatian,Romania},
  Mac{Cyrillic,Ukraine,Greek,Turkish},
  Macintosh
Semitic languages
  ISO-8859-{6,8}, CP{1255,1256}, Mac{Hebrew,Arabic}
Japanese
  EUC-JP, SHIFT-JIS, CP932, ISO-2022-JP, ISO-2022-JP-2, ISO-2022-JP-1
Chinese
  EUC-CN, HZ, GBK, EUC-TW, BIG5, CP950, ISO-2022-CN, ISO-2022-CN-EXT
Korean
  EUC-KR, CP949, ISO-2022-KR
Armenian
  ARMSCII-8
Georgian
  Georgian-Academy, Georgian-PS
Thai
  TIS-620, CP874, MacThai
Laotian
  MuleLao-1, CP1133
Vietnamese
  VISCII, TCVN, CP1258
Platform specifics
  HP-ROMAN8, NEXTSTEP
Full Unicode
  UTF-8, UCS-2, UCS-2BE, UCS-2LE, UCS-4, UCS-4BE, UCS-4LE,
  UTF-16, UTF-16BE, UTF-16LE, UTF-7, JAVA
Full Unicode, in terms of `uint16_t' or `uint32_t'
  (with machine dependent endianness and alignment)
   UCS-2-INTERNAL, UCS-4-INTERNAL


%prep
rm -rf $RPM_BUILD_ROOT

%setup
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib
mkdir -p $RPM_BUILD_ROOT%{prefix}/include
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man/man3
make prefix=$RPM_BUILD_ROOT%{prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 6 2001 Hirofumi Takeda <takepin@turbolinux.co.jp>                  
- remove man files (conflict with man-pages package)                                  

* Tue Sep 19 2000 Hirofumi Takeda <takepin@turbolinux.co.jp>                  
- rewrite spec file for FHS 2.1                                              

* Fri Aug 11 2000 SL Baur  <steve@turoblinux.co.jp>
- fixes for rpm-4

* Thu Jul 27 2000 Hirofumi Takeda <takepin@turbolinux.co.jp>
- deleted /usr/include/iconv.h (conflicts with glibc-devel) (#1120)

* Tue Jun 6 2000 Hirofumi Takeda <takepin@turbolinux.co.jp>
- modified spec file
- updated to 1.3

* Thu Mar 30 2000 Takeshi Aihana <aihana@turbolinux.co.jp>
- initial package


%pre
if [ -f /usr/include/iconv.h ]; then
  mv /usr/include/iconv.h /usr/include/iconv.h.rpmsave
fi


%post
if [ -f /usr/include/iconv.h.rpmsave ]; then
  mv /usr/include/iconv.h.rpmsave /usr/include/iconv.h
fi


%files
%defattr(-,root,root)
%doc AUTHORS COPYING.LIB ChangeLog DESIGN NEWS NOTES PORTS README README.win32
%{prefix}/lib/libiconv.la
%{prefix}/lib/libiconv.so
%{prefix}/lib/libiconv.so.2
%{prefix}/lib/libiconv.so.2.*
%{prefix}/lib/libiconv_plug.so
#%{prefix}/include/iconv.h
#%{_mandir}/man3/iconv.3*
#%{_mandir}/man3/iconv_close.3*
#%{_mandir}/man3/iconv_open.3*
