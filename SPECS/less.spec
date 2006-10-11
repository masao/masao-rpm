Summary: A text file browser similar to more, but better.
Name: less
Version: 382
Release: 4
License: GPL
Group: Applications/Text
Source: http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
Source1: lesspipe.sh
Source2: less.sh
Source3: less.csh

Patch0:	less-382-ncursesw.patch
Patch1: less-382-iso258.patch
Patch2: less-382-iso258-259.patch
Patch3: less-382-iso259-260.patch
Patch4: less-382-iso260-261.patch
Patch5: less-382-iso261-262.patch

URL: http://www.greenwoodsoftware.com/less/
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: ncurses-devel

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi). 

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.

%prep
%setup -q
%patch0 -p1 -b .ncursesw
%patch1 -p1 -b .iso258
%patch2 -p1 -b .iso259
%patch3 -p1 -b .iso260
%patch4 -p1 -b .iso261
%patch5 -p1 -b .iso262
chmod -R a+w *

%build
%configure
make CC="gcc $RPM_OPT_FLAGS -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" datadir=%{_docdir}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
strip -R .comment $RPM_BUILD_ROOT/usr/bin/less
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -c -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/
install -c -m 755 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -c -m 755 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d

%files
%defattr(-,root,root)
/etc/profile.d/*
/usr/bin/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 11 2006 Masao Takaku <masao@nii.ac.jp>
- add iso262 patches

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 29 2004 Karsten Hopp <karsten@redhat.de> 382-3
- remove old stuff from /etc/profile.d/less.*, fixes #109011

* Tue Mar 02 2004 Karsten Hopp <karsten@redhat.de> 382-1.1 
- build for FC1

* Sat Feb 14 2004 Karsten Hopp <karsten@redhat.de> 382-1
- new upstream version

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 15 2004 Karsten Hopp <karsten@redhat.de> 381-2 
- drop iso247 patch, doesn't work

* Wed Jun 11 2003 Karsten Hopp <karsten@redhat.de> 381-1
- new version with rewritten iso247 patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 28 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- fix korean #79977
- add new less.sh from #89780, s/ko/korean/ and write .csh script
- add patch from #91661: /japanses/japanese-euc/

* Tue Feb  4 2003 Tim Waugh <twaugh@redhat.com> 378-7
- Part of multibyte patch was missing; fixed.

* Mon Feb  3 2003 Tim Waugh <twaugh@redhat.com> 378-6
- Fix underlining multibyte characters (bug #83377).

* Thu Jan 30 2003 Karsten Hopp <karsten@redhat.de> 378-5
- removed older, unused patches
- add patch from Yukihiro Nakai to fix display of japanese text
  (#79977)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 18 2002 Karsten Hopp <karsten@redhat.de>č
- removed default 'cat' from lesspipe.sh as it breaks 'v' and 'F' keys 
  (#79921)

* Fri Dec  6 2002 Nalin Dahyabhai <nalin@redhat.com> 378-2
- add a default case to lesspipe so that it shows other kinds of files

* Mon Nov 04 2002 Karsten Hopp <karsten@redhat.de>
- less-378
- added some debian patches
- show image info instead of binary garbage when viewing images

* Fri Oct 05 2001 Karsten Hopp <karsten@redhat.de>
- fix line numbering (less -N filename), caused by
  a broken i18n patch

* Tue Sep 04 2001 Karsten Hopp <karsten@redhat.de>
- recompile with large file support (#52945)

* Tue Jul 24 2001 Karsten Hopp <karsten@redhat.de>
- fix #49506 (BuildRequires)

* Mon Jun 25 2001 Nalin Dahyabhai <nalin@redhat.com>
- fixup eline patch to initialize result correctly

* Mon Jun 25 2001 Karsten Hopp <karsten@redhat.de>
- update URLs
- Copyright -> License
- fix #43348 (crashes when searching for /<)
- fix #39849 (
  _ ignores LESSCHARDEF in displaying characters,
  _ prefaces sequences of one or "high" characters with a capital "A")

* Mon Feb  5 2001 Yukihiro Nakai <ynakai@redhat.com>
- Update less.sh, less.csh to set JLESSCHARSET=japanese
  when LANG=ja??

* Mon Feb  5 2001 Matt Wilson <msw@redhat.com>
- changed the less-358+iso247-20001210.diff patch to use strcasecmp when
  comparing locale names

* Thu Feb 01 2001 Karsten Hopp <karsten@redhat.de>
- fixed character translations (bugzilla #24463)

* Wed Jan 31 2001 Karsten Hopp <karsten@redhat.de>
- fixed lesspipe (bugzilla #17456 #25324)

* Tue Dec 12 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with new ncurses

* Mon Dec 11 2000 Yukihiro Nakai <ynakai@redhat.com>
- Add Japanese patch with ia64 support.

* Mon Nov 27 2000 Karsten Hopp <karsten@redhat.de>
- rebuild with new ncurses
- fix Bug #21288

* Mon Nov 13 2000 Karsten Hopp <karsten@redhat.de>
- fixed handling of manpages of type *.1x.gz
- added support for cpio packages

* Thu Sep 14 2000 Than Ngo <than@redhat.com>
- added new lesspipe.sh (Bug #17456)

* Wed Aug 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- support files with spaces in their names (Bug #16777)

* Tue Aug  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Support gzipped man pages in lesspipe.sh (Bug #15610)

* Thu Aug  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Tweak init script (Bug #14622)

* Thu Jul 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Oops, actually apply the patch for 9443. ;)

* Wed Jul 26 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up messed output if a user outputs anything in ~/.bashrc or the
  likes (Bug #9443)
- handle RPM_OPT_FLAGS

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 358

* Mon Jun 26 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- FHSify

* Fri Apr 14 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 354

* Mon Mar 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to v352

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Tue Jan 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to v346
- Update download URL
- use the configure marcro
- strip binary
- fix up lesspipe stuff (Bug #8750 and a couple of non-reported bugs)
  (Karsten, did I mention I'll kill you when you return from SAP? ;) )

* Sun Jan 07 2000 Karsten Hopp <karsten@redhat.de>
- added lesspipe.sh to show listings of package
  contents instead of binary output.

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- less finally gets maintenance, upgraded to 340

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Tue Mar 16 1999 Preston Brown <pbrown@redhat.com>
- removed ifarch axp stuff for /bin/more, more now works on alpha properly.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 332 and built for Manhattan
- added buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
