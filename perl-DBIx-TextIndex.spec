#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# Requires configured MySQL local database

%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	TextIndex
Summary:	DBIx::TextIndex - Perl extension for full-text searching in SQL databases
Summary(pl.UTF-8):	DBIx::TextIndex - rozszerzenie do pełnotekstowego przeszukiwania baz SQL
Name:		perl-DBIx-TextIndex
Version:	0.25
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af19205380c2d845f0cb095ac93c7300
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Text::Balanced) # core perl module since 5.8
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-Exception-Class
#BuildRequires:	perl-Text-Unaccent # Not in PLD yet
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
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
