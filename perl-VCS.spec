%include	/usr/lib/rpm/macros.perl
Summary:	VCS perl module
Summary(pl):	Modu� perla VCS
Name:		perl-VCS
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/VCS/VCS-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
VCS - Library for generic Version Control System access in Perl.

%description -l pl
VCS - biblioteka umo�liwiaj�ca dost�p do systemu kontroli wersji (VCS)
z poziomu perla.

%prep
%setup -q -n VCS-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

cp -ar examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/VCS
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/VCS.pm
%{perl_sitelib}/VCS
%{perl_sitearch}/auto/VCS

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
