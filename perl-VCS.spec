%include	/usr/lib/rpm/macros.perl
Summary:	VCS perl module
Summary(pl):	Modu³ perla VCS
Name:		perl-VCS
Version:	0.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/VCS/VCS-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCS - Library for generic Version Control System access in Perl.

%description -l pl
VCS - biblioteka umo¿liwiaj±ca dostêp do systemu kontroli wersji (VCS)
z poziomu perla.

%prep
%setup -q -n VCS-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/VCS.pm
%{perl_sitelib}/VCS
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
