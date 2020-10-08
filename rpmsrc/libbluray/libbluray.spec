%global build_pdf_doc 0

Name:           libbluray
Version:        1.1.2
Release:        2%{?dist}
Summary:        Library to access Blu-Ray disks for video playback 
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbluray.html

Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libbluray-0.8.0-no_doxygen_timestamp.patch

BuildRequires:  ant
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  graphviz
BuildRequires:  java-devel >= 1:1.8.0
BuildRequires:  jpackage-utils
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  texlive-latex

%description
This package is aiming to provide a full portable free open source Blu-Ray
library, which can be plugged into popular media players to allow full Blu-Ray
navigation and playback on Linux. It will eventually be compatible with all
current titles, and will be easily portable and embeddable in standard players
such as MPlayer and VLC.

%package        bdj
Summary:        BDJ support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       java-headless >= 1:1.8.0
Requires:       jpackage-utils

%description    bdj
The %{name}-bdj package contains the jar file needed to add BD-J support to
%{name}. BD-J support is still considered alpha.

%package        utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains test utilities for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .no_timestamp


%build
export JDK_HOME="%{_jvmdir}/java-1.8.0"

autoreconf -vif
%configure --disable-static \
%if %{build_pdf_doc}
           --enable-doxygen-pdf \
%else
           --disable-doxygen-pdf \
%endif
           --disable-doxygen-ps \
           --enable-doxygen-html \
           --enable-examples

make %{?_smp_mflags}
make doxygen-doc
# Remove uneeded script
rm -f doc/doxygen/html/installdox 

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Install test utilities
for i in bdjo_dump bdsplice clpi_dump hdmv_test index_dump libbluray_test \
         list_titles mobj_dump mpls_dump sound_dump
do install -Dp -m 0755 .libs/$i %{buildroot}%{_bindir}/$i; done;

install -Dp -m755 .libs/bdj_test %{buildroot}%{_bindir}/bdj_test;

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README.txt
%{_libdir}/*.so.2*

%files bdj
%{_javadir}/libbluray-j2se-%{version}.jar
%{_javadir}/libbluray-awt-j2se-%{version}.jar

%files utils
%{_bindir}/*

%files devel
%doc doc/doxygen/html
%if %{build_pdf_doc}
%doc doc/doxygen/%{name}.pdf
%endif
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Xavier Bachelot <xavier@bachelot.org> 1.1.2-1
- Update to 1.1.2 (RHBZ#1718617).

* Mon Apr 08 2019 Xavier Bachelot <xavier@bachelot.org> 1.1.1-1
- Update to 1.1.1 (RHBZ#1676566).

* Tue Feb 12 2019 Xavier Bachelot <xavier@bachelot.org> 1.1.0-1
- Update to 1.1.0 (RHBZ#1676566).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Simone Caronni <negativo17@gmail.com> - 1.0.2-2
- Package no longer builds with OpenJDK 1.7, require 1.8 also for RHEL/CentOS.

* Sun Dec 03 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.2-1
- Update to 1.0.2.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.1-1
- Update to 1.0.1.

* Thu Mar 02 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.0-1
- Update to 1.0.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Xavier Bachelot <xavier@bachelot.org> 0.9.3-3
- Add patch to fix search paths for libjvm.so (RHBZ#1380437).

* Sat Dec 03 2016 Simone Caronni <negativo17@gmail.com> - 0.9.3-2
- Use autotools to get rid of RPATH.
- Fix Java build requirements for RHEL/CentOS 7.
- Clean up SPEC file, rpmlint fixes.
- Add license macro.

* Wed May 18 2016 Xavier Bachelot <xavier@bachelot.org> 0.9.3-1
- Update to 0.9.3.

* Tue Mar 01 2016 Xavier Bachelot <xavier@bachelot.org> 0.9.2-1
- Update to 0.9.2 (RHBZ#1287343).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Dominik Mierzejewski <rpm@greysector.net> - 0.9.1-1
- update to 0.9.1
- mark license text as such

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Karsten Hopp <karsten@redhat.com> 0.8.0-2git}
- openjdk is available on all archs now, drop ppc* special cases

* Wed Apr 29 2015 Xavier Bachelot <xavier@bachelot.org> 0.8.0-1
- Update to 0.8.0 (RHBZ#1217475).

* Tue Jan 27 2015 Xavier Bachelot <xavier@bachelot.org> 0.7.0-1
- Update to 0.7.0.

* Thu Sep 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.6.2-1
- Update to 0.6.2.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Xavier Bachelot <xavier@bachelot.org> 0.6.1-1
- Update to 0.6.1.
- Fix building with openJDK 8.

* Wed Jun 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.6.0-1
- Update to 0.6.0.

* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> 0.5.0-5
- Tweak the Release: tag to accomodate rpmdev-bumpspec.

* Fri Feb 21 2014 Xavier Bachelot <xavier@bachelot.org> 0.5.0-4
- Requires: java-headless for Fedora 21+ (RHBZ#1068351).
- Modernize specfile.

* Fri Jan 10 2014 Xavier Bachelot <xavier@bachelot.org> 0.5.0-3
- Disable BD-J support for ppc64le arch (RHBZ#1051604).

* Sun Dec 22 2013 Xavier Bachelot <xavier@bachelot.org> 0.5.0-2
- Fix build on EL6 (BR: java7-devel instead of java-devel).

* Sat Dec 21 2013 Xavier Bachelot <xavier@bachelot.org> 0.5.0-1
- Update to 0.5.0.

* Tue Nov 26 2013 Xavier Bachelot <xavier@bachelot.org> 0.4.0-2
- Move test utilities to their own subpackage to avoid multilib conflict.
  Fix RHBZ#1034307.
- Rename java subpackage to bdj.
- Remove obsolete xine-lib bluray input plugin from doc files.

* Fri Sep 20 2013 Xavier Bachelot <xavier@bachelot.org> 0.4.0-1
- Update to 0.4.0.
- Fix rpath issues with some test utilities.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Xavier Bachelot <xavier@bachelot.org> 0.2.3-1
- Update to 0.2.3.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Xavier Bachelot <xavier@bachelot.org> 0.2.2-3
- Don't build pdf doc, it breaks multilib (see RHBZ#835952).

* Tue Jun 12 2012 Xavier Bachelot <xavier@bachelot.org> 0.2.2-2
- Fix multilib conflict in doxygen docs (RHBZ#831401).

* Tue Mar 20 2012 Xavier Bachelot <xavier@bachelot.org> 0.2.2-1
- Update to 0.2.2.

* Tue Mar 20 2012 Karsten Hopp <karsten@redhat.com> 0.2.1-4
- ppc(64) has no java-1.7.0-open yet, disable java subpackage on both PPC archs

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2.1-3
- make build non-fatal when using doxygen-1.8 (doesn't produce installdox anymore)

* Wed Feb 01 2012 Xavier Bachelot <xavier@bachelot.org> 0.2.1-2
- Rebuild for openjdk 7.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 Xavier Bachelot <xavier@bachelot.org> 0.2.1-1
- First upstream official release.
- Fix BD-J build (missing files in upstream tarball).
- Have subpackages require an arch-specific base package.

* Sun Oct 23 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.7.20111023gite037110f11e70
- Update to latest snapshot.

* Sat Jul 16 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.6.20110710git51d7d60a96d06
- Don't build java subpackage on ppc64, no java-1.6.0-devel package.

* Sun Jul 10 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.5.20110710git51d7d60a96d06
- Update to latest snapshot.

* Sat May 14 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.4.20110514git46ee2766038e9
- Update to latest snapshot.
- Drop -static subpackage.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-0.3.20110126gitbbf11e43bd82e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.2.20110126gitbbf11e43bd82e
- Update to latest snapshot.
- Split the BDJ support to a -java subpackage.

* Fri Jan 07 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.1.20110107git0e5902ff9a6f1
- Update to latest snapshot.
- Add BR: libxml2-devel for metadata parser.
- Add BR: graphviz for doc generation.

* Thu Oct 28 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.3.20101028gitc32862b77dea4
- Update to latest snapshot.
- Install BDJ jar.

* Thu Oct 21 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.2.20101021git144a204c02687
- Fix release tag.
- Update to latest snapshot.

* Thu Aug 19 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.1.20100819
- Initial Fedora release.
