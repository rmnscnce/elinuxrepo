%global lcname muparser
%global owner beltoforion
Name:           muParser
Summary:        A fast math parser library
Version:        2.2.5
Release:        1%{?dist}.elinuxrepo
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
URL:            http://beltoforion.de/article.php?a=muparser
License:        MIT
Group:          Development/Libraries
Source0:        https://github.com/%{owner}/%{lcname}/archive/v%{version}/%{lcname}-%{version}.tar.gz


%package devel
Summary:        Development and doc files for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig
Group:          Development/Libraries

%description
Many applications require the parsing of mathematical expressions.
The main objective of this project is to provide a fast and easy way
of doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode
and precalculating constant parts of it.

%description devel
Development files and the documentation

%prep
%setup -q -n %{lcname}-%{version}

%build
%configure --enable-shared=yes --enable-debug=no --enable-samples=no
make CXXFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
#mv docs/html .
#dos2unix *.txt html/{script,sources,misc}/*
#chmod ugo-x html/{images,sources,misc}/*

%install
make libdir=$RPM_BUILD_ROOT%{_libdir} prefix=$RPM_BUILD_ROOT/usr install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc Changes.txt
%doc License.txt
%{_libdir}/lib%{lcname}.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{lcname}.so
%{_libdir}/pkgconfig/muparser.pc

%changelog
* Tue Nov 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.5-8
- rebuilt to fix FTBFS rhbz #1604900 #1316595 and #1448721

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.5-1
- Rebuilt for new upstream release 2.2.5, fixes rhbz #1316595

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 12 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.3-3
- Fixed typo in summary of -devel package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Eric Smith <brouhaha@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Eric Smith <eric@brouhaha.com> - 2.2.2-1
- Update to 2.2.2
- Upstream source distribution is now a .zip file
- Upstream version number policy is now that the release version matches
  the .so versioning
- Clean up spec to modern standards (no clean section or BuildRoot tag, etc.)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Fabian Deutsch <fabiand@fedoraproject.org> - 1.34-1
- Update to 1.34

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Frank Büttner <frank-buettner@gmx.net> - 1.32-1
- update to 1.32

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 08 2008 Jesse Keating <jkeating@redhat.com> - 1.28-4
- Fix the gcc4.3 errors.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.28-3
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.28-2
- Rebuild for selinux ppc32 issue.

* Sat Jul 14 2007 Frank Büttner <frank-buettner@gmx.net> - 1.28-1
 - update to 1.28
* Fri Jun 15 2007 Frank Büttner <frank-buettner@gmx.net> - 1.27-5%{?dist}
 - fix bug #244309
* Fri Jun 08 2007 Frank Büttner <frank-buettner@gmx.net> - 1.27-4%{?dist}
 - fix depend on pkgconfig
* Wed Jun 06 2007 Frank Büttner <frank-buettner@gmx.net> - 1.27-3%{?dist}
 - clean build root before run install part
 - fix missing pkconfig file
* Thu May 17 2007 Frank Büttner <frank-buettner@gmx.net> - 1.27-2%{?dist}
  - fix missing post -p /sbin/ldconfig
  - fix the double doc files
  - fix missing compiler flags
  - fix wrong file encoding of the doc files
* Wed May 16 2007 Frank Büttner <frank-buettner@gmx.net> - 1.27-1%{?dist}
  - start
