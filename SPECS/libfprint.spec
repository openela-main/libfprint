Name:           libfprint

Version:        1.90.7
Release:        1%{?dist}
Summary:        Toolkit for fingerprint scanner

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz
ExcludeArch:    s390 s390x

BuildRequires:  rpm-build
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests
BuildRequires:  cairo-devel
BuildRequires:  python3-cairo python3-gobject
#BuildRequires:  umockdev

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-v%{version}

%build
# Include the virtual image driver for integration tests
%meson -Dx11-examples=false -Ddrivers=all
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%check
%meson_test

%files
%license COPYING
%doc NEWS TODO THANKS AUTHORS README
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevrulesdir}/60-libfprint-2-autosuspend.rules

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-2.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/

%changelog
* Wed Jan 20 14:11:30 CET 2021 Benjamin Berg <bberg@redhat.com> - 1.90.7-1
- New upstream release 1.90.7
  Related: #1888181

* Mon Dec 14 2020 Benjamin Berg <bberg@redhat.com> - 1.90.6-1
- New upstream release 1.90.6
  Related: #1888181

* Tue Dec 08 2020 Benjamin Berg <bberg@redhat.com> - 1.90.5-2
- New upstream release 1.90.5
  Related: #1888181

* Mon Jan 20 2020 Benjamin Berg <bberg@redhat.com> - 1.90.0-4
- Add patch to fix unit-test failure

* Wed Jan 15 2020 Benjamin Berg <bberg@redhat.com> - 1.90.0-3
- Pull in upstream fixes from the not-yet released 1.90.1
- Related: rhbz1791256

* Fri Nov 22 2019 Benjamin Berg <bberg@redhat.com> - 1.90.0-2
- Add patch to remove debug spew from udev rules
- Add patch to fix compilation error
- Related: rhbz1740752

* Wed Oct 09 2019 Benjamin Berg <bberg@redhat.com> - 1.90.0-1
+ libfprint-1.90.0-1
- Update to 1.90.0
- Resolves: rhbz1740752

* Tue Jul 17 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.2-1
+ libfprint-0.8.2-1
- Update to 0.8.2

* Fri Jun 15 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.1-1
+ libfprint-0.8.1-1
- Update to 0.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Bastien Nocera <bnocera@redhat.com> - 0.7.0-1
+ libfprint-0.7.0-1
- Update to 0.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Bastien Nocera <bnocera@redhat.com> 0.6.0-1
- Update to 0.6.0

* Wed Dec 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-5
- error opening ATTR{/sys/devices/pci0000:00/0000:00:1a.0/usb1/1-1/1-1.3/1-1.3:1.0/power/control} for writing (#950205)
- %%build: --disable-silent-rules

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-2
- Drop INSTALL from docs.

* Sun Aug 11 2013 Bastien Nocera <bnocera@redhat.com> 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Bastien Nocera <bnocera@redhat.com> 0.5.0-1
- Update to 0.5.0
- Re-add not useless udev rules

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Matthias Clasen <mclasen@redhat.com> - 0.4.0-4
- Drop broken and useless udev rules (#744637)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Adam Jackson <ajax@redhat.com> 0.4.0-2
- Rebuild without Requires: ConsoleKit, going away in F17

* Thu Nov 10 2011 Bastien Nocera <bnocera@redhat.com> 0.4.0-1
- Update to 0.4.0

* Mon Nov 07 2011 Adam Jackson <ajax@redhat.com> 0.3.0-3
- Rebuild for libpng 1.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Bastien Nocera <bnocera@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Aug 19 2010 Bastien Nocera <bnocera@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Jun 30 2010 Matthew Garrett <mjg@redhat.com> 0.1.0-16.pre3
- Fix #505438 to avoid message on boot on some systems

* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 0.1.0-16.pre2
- Add README to package

* Wed Jan 20 2010 Bastien Nocera <bnocera@redhat.com> 0.1.0-15.pre2
- Require hal-filesystem for the fdi file

* Tue Dec 01 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-14.pre2
- Update AES1610 patch

* Mon Nov 30 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-13.pre2
- Add aes1610 driver (#499732)

* Thu Oct 01 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-12.pre2
- Update udev autosuspend rules and disable SGS Thomson reader

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.0-11.pre2
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-9.pre2
- Use gdk-pixbuf for image manipulation instead of ImageMagick (#472103)

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-8.pre2
- Update to 0.1.0-pre2

* Tue Jun 09 2009 Matthew Garrett <mjg@redhat.com> 0.1.0-7.pre1
- fprint-add-udev-rules.patch - build udev rules for autosuspend
- move hal fdi into the main package rather than -devel
- add autoreconf as a build depend while carrying the udev diff

* Tue Apr 21 2009 Karsten Hopp <karsten@redhat.com> 0.1.0-6.pre1.1
- Excludearch s390 s390x, we don't have USB devices there and this package
  doesn't build without USB support

* Mon Mar 09 2009 pingou <pingou@pingoured.fr> - 0.1.0-6.pre1
- Rebuilt for rawhide

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.0-4.pre1
- rebuild with new openssl

* Tue Nov 25 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-3.pre1
- Fix possible crasher in libfprint when setting up the fds for polling

* Mon Nov 24 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-2.pre1
- And add some API docs

* Tue Nov 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-1.pre1
- Fix build

* Tue Nov 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-0.pre1
- Update to 0.1.0-pre1

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-6
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-5
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-4
- Update the Build Requires due to the change on ImageMagick

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.5-3
- Autorebuild for GCC 4.3

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-2
- Change on the BuildRequires

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-1
- Update to version 0.0.5

* Sat Dec 01 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-3
- Changes on the Requires

* Sun Nov 25 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-2
- Changes on the Requires

* Sat Nov 24 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-1
- First release
