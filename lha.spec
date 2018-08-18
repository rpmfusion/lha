%global commit  6f6cbc189d23b7c3a8636819f5796654f188764e
%global date 20161015
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})

Name:           lha
Version:        1.14i
Release:        33%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Archiving and compression utility for LHarc/lha/lzh archives
Group:          Applications/Archiving
License:        Distributable
URL:            https://github.com/jca02266/%{name}
Source0:        %url/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  automake
BuildRequires:  gcc

%description
LHA is an archiving and compression utility for LHarc/lha/lzh format archives.


%prep
%autosetup -n %{name}-%{commit}
autoreconf -fiv

# Rename doc files to better represent encoding which is EUC (jp)
cd olddoc/
mv change-114e.txt change-114e.euc
mv change-114g.txt change-114g.euc
mv change-114h.txt change-114h.euc
mv change-114i.txt change-114i.euc

%build
%configure
%make_build

%check
pushd tests
make %{?_smp_mflags} check-local
popd

%install
%make_install
mkdir -p %{buildroot}%{_mandir}/ja/mann
install -m 644 man/lha.n %{buildroot}%{_mandir}/ja/mann/lha.n

%files
%doc olddoc/change-114* olddoc/CHANGES.euc
%doc olddoc/PROBLEMS.euc olddoc/README.euc
%{_bindir}/lha
%{_mandir}/man1/lha.1.*
%lang(ja) %{_mandir}/ja/mann/lha.n*

%changelog
* Sat Aug 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14i-33.20161015git6f6cbc1
- Switch to upstream git source

* Fri Aug 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14i-32
- Add missing stdlib include
- Clean up spec file

* Fri Aug 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14i-31
- Rebuild because of the binutils screw up

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.14i-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.14i-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14i-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14i-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.14i-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.14i-25
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.14i-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.14i-23
- rebuild for new F11 features

* Thu Jul 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.14i-22
- Rebuild for buildsys cflags issue

* Wed Jul 23 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.14i-21
- Release bump for rpmfusion build

* Sun Jan 14 2007 Ian Chapman <packages@amiga-hardware.com> 1.14i-20%{?dist}
- Initial dribble release
- Aesthetic spec clean-ups for publishing in dribble
- Use %%{?_smp_mflags}
- Use %%{optflags}
- Changed the description (it's saner IMHO)
- Include changelogs
- Dropped MACHINES*, useless to end user
- Changed license field from freeware to distributable

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.14i-19.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.14i-19.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Mar 05 2005 Than Ngo <than@redhat.com> 1.14i-19
- rebuilt

* Wed Feb 09 2005 Than Ngo <than@redhat.com> 1.14i-18
- rebuilt

* Fri Sep 10 2004 Than Ngo <than@redhat.com> 1.14i-17
- security vulnerabilities CAN-2004-0769, CAN-2004-0771, CAN-2004-0694, CAN-2004-0745

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 21 2004 Than Ngo <than@redhat.com> 1.14i-15
- fix segmentation fault on ia64

* Wed May 05 2004 Than Ngo <than@redhat.com> 1.14i-14
- fix security vulnerabilities, CAN-2004-0234, CAN-2004-0235

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 20 2003 Than Ngo <than@redhat.com> 1.14i-11
- add patch file from Matt Wilson, bug #91206

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.14i-8
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 1.14i-6
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Feb 27 2002 Than Ngo <than@redhat.com> 1.14i-4
- rebuild

* Tue Jan 29 2002 Than Ngo <than@redhat.com> 1.14i-3
- rebuild in rawhide

* Tue Sep 25 2001 Than Ngo <than@redhat.com> 1.14i-1
- update to 1.14i (bug #52779)

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- rebuilt for the distro

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri May 12 2000 Tim Powers <timp@redhat.com>
- rebuilt for Powertools-7.0

* Wed Jan 19 2000 Bill Nottingham <notting@redhat.com>
- add some more docs

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 11)

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- this package will never change.
- changed groups

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- add english doco.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- removed man page, wasn't ASCII and caused more harm than good
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
