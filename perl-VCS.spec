%include	/usr/lib/rpm/macros.perl
Summary:	VCS perl module
Summary(pl):	Modu³ perla VCS
Name:		perl-VCS
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/VCS/VCS-%{version}.tar.gz
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/diff-hist
%{perl_sitelib}/VCS.pm
%{perl_sitelib}/VCS
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
