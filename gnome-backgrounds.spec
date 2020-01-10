Name: gnome-backgrounds
Version: 3.28.0
Release: 1%{?dist}
Summary: Desktop backgrounds packaged with the GNOME desktop

License: GPLv2
URL: http://www.gnome.org
Source0: https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz

BuildArch: noarch
BuildRequires: gettext
BuildRequires: meson

%description
The gnome-backgrounds package contains images and tiles
to use for your desktop background which are packaged
with the GNOME desktop.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images

# all translations are merged back into xml by intltool
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%license COPYING
%doc NEWS README AUTHORS
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/*

%changelog
* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Resolves: #1569727

* Fri Mar 10 2017 Matthias Clasen <mclasen@redhat.com> - 3.22.1-1
- Rebase to 3.22.1
  Resolves: rhbz#1386877

* Fri Jul 01 2016 Kalev Lember <klember@redhat.com> - 3.14.1-2
- Update translations
- Resolves: #1304293

* Wed Apr 29 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Resolves: #1174385

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.1-3
- Mass rebuild 2013-12-27

* Wed Jul 17 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-2
- Rebuild without unused patches

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> 2.32.0-1
- Update to 2.32.0

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Mon Mar  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.0-2
- Drop ownership of a directory that is now owned by filesystem

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-3
- Co-own /usr/share/backgrounds instead of requiring desktop-backgrounds-basic

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Lennart Poettering <lpoetter@redhat.com> - 2.24.0-3
- Include AUTHORS file in package

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Don't ship unneeded translations

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.0-1
- Update to 2.23.0

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-2
- Small fixes from package review

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3
- Update the license field

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2
- Require desktop-backgrounds-basic for directory ownership

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-3
- Add missing BuildRequires

* Thu Jun  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-2
- Update to 2.14.2.1

* Mon Mar 13 2005 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-1
- Initial build.

