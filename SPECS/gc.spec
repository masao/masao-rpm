Summary: C++ Garbage Collector	
Summary(ja): C++ ガーベージコレクションライブラリ
Name:    gc	
Version: 6.4
Release: masao1
Group:	 System Environment/Libraries
License: BSD
Url:     http://www.hpl.hp.com/personal/Hans_Boehm/gc/	
Source:  http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/%{name}%{version}.tar.gz
Prefix:	 %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The Boehm-Demers-Weiser conservative garbage collector can be used as a garbage 
collecting replacement for C malloc or C++ new.

%package devel
Summary: Libraries and header files for gc development 
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
Libraries and header files for gc development.


%prep
%setup -q -n %{name}%{version}

%build
%configure --enable-cplusplus 
make %{?_smp_mflags}
make check


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install 
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -m644 doc/gc.man $RPM_BUILD_ROOT%{_mandir}/man3/gc.3
## Unpackaged files
rm -rf $RPM_BUILD_ROOT%{_datadir}/gc
rm -f  $RPM_BUILD_ROOT%{_libdir}/lib*.la


%clean
rm -rf 	"$RPM_BUILD_ROOT"


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files 
%defattr(-,root,root)
%doc doc/README*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc doc/*.html
%dir %{_includedir}/gc
%{_includedir}/gc/*
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_mandir}/man?/*


%changelog
* Thu Feb  3 2005 Masao Takaku <masao@nii.ac.jp> 6.4-masao1
- update to gc6.4
* Sun Jan 18 2004 Daisuke SUZUKI <daisuke@linux.or.jp> 6.2-0vl1
- initial build for Vine Linux
