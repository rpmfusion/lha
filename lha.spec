Name:           lha
Version:        1.14i
Release:        21%{?dist}
Summary:        Archiving and compression utility for LHarc/lha/lzh archives
Group:          Applications/Archiving
License:        Distributable
URL:            http://www2m.biglobe.ne.jp/~dolphin/lha/prog/
Source0:        http://www2m.biglobe.ne.jp/~dolphin/%{name}/prog/%{name}-114i.tar.gz
Patch0:         lha-1.14i-symlink.patch
Patch1:         lha-1.14i-malloc.patch
Patch2:         lha-1.14i-sec.patch
Patch3:         lha-1.14i-dir_length_bounds_check.patch
Patch4:         lha-1.14i-sec2.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LHA is an archiving and compression utility for LHarc/lha/lzh format archives.


%prep
%setup -qn lha-114i

%patch0 -p1 -b .symlink
%patch1 -p1 -b .malloc
# security fixes
%patch2 -p1 -b .sec
%patch3 -p1 -b .sec
%patch4 -p1 -b .sec

# Rename doc files to better represent encoding which is EUC (jp)
mv change-114e.txt change-114e.euc
mv change-114g.txt change-114g.euc
mv change-114h.txt change-114h.euc
mv change-114i.txt change-114i.euc


%build
make %{?_smp_mflags} OPTIMIZE="%{optflags} -DSUPPORT_LH7 -DMKSTEMP"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 src/lha %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc change-114* CHANGES.euc PROBLEMS.euc README.euc
%{_bindir}/lha


%changelog
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
