#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires configured local MySQL database)
#
%define		pdir	DBIx
%define		pnam	TextIndex
Summary:	DBIx::TextIndex - Perl extension for full-text searching in SQL databases
Summary(pl.UTF-8):	DBIx::TextIndex - rozszerzenie do pełnotekstowego przeszukiwania baz SQL
Name:		perl-DBIx-TextIndex
Version:	0.28
Release:	17
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1533f1e0c736988b22b29bcd4ba739a8
URL:		http://search.cpan.org/dist/DBIx-TextIndex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-Text-Balanced
BuildRequires:	perl-Text-Unaccent
%endif
Requires:	perl-DBI >= 1.48-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::TextIndex was developed for doing full-text searches on BLOB
columns stored in a database. Almost any database with BLOB and DBI
support should work with minor adjustments to SQL statements in the
module.

%description -l pl.UTF-8
Moduł DBIx::TextIndex służy do przeprowadzania pełnotekstowych
przeszukiwań kolumn BLOB zapisanych w bazie danych. Prawie każda baza
danych z obsługą BLOB i DBI powinna działać po niewielkich poprawkach
wyrażeń SQL w module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf eg/README
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/DBIx/TextIndex/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/DBIx/*.pm
%{perl_vendorarch}/DBIx/TextIndex
%dir %{perl_vendorarch}/auto/DBIx/TextIndex
%attr(755,root,root) %{perl_vendorarch}/auto/DBIx/TextIndex/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
