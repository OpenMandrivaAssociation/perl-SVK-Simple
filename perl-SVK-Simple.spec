%define upstream_name    SVK-Simple
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Simple interface to svk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GU/GUGOD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Field)
BuildRequires:	perl-SVK
BuildRequires:	perl(Spiffy)
BuildArch:	noarch

%description
Although SVK.pm itself is already simple enough, there still are some misc 
requirements in the svk script which is not included in SVK.pm. This module 
helps people who wants to write some SVK applications. It provides a simple 
SVK object loader, so people will not have to handle XD initialization.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jul 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 399314
- update to 0.03
- using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-11mdv2009.0
+ Revision: 258394
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-10mdv2009.0
+ Revision: 246481
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-8mdv2008.1
+ Revision: 171030
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Michael Scherer <misc@mandriva.org> 0.02-7mdv2008.0
+ Revision: 81733
- rebuild


* Wed Jul 05 2006 Olivier Blin <oblin@mandriva.com> 0.02-6mdv2007.0
- improve URL
- BuildRequires perl-devel only when < 10.1
- drop wrong perl-Clone require (should be in perl-SVK)

* Wed Jul 05 2006 Olivier Blin <oblin@mandriva.com> 0.02-5mdv2007.0
- add explicit perl-Clone requires, since rpm's perl.req skips
  "require" statements that aren't flush against the left edge

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.02-4mdk
- Do not ship empty dir

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 0.02-1mdk
- First mandriva package

