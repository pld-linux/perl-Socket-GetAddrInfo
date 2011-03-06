#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Socket
%define	pnam	GetAddrInfo
Summary:	Socket::GetAddrInfo - RFC 2553's getaddrinfo and getnameinfo functions
Summary(pl.UTF-8):	Socket::GetAddrInfo - funkcje getaddrinfo i getnameinfo zgodne z RFC 2553
Name:		perl-Socket-GetAddrInfo
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Socket/PEVANS/Socket-GetAddrInfo-%{version}.tar.gz
# Source0-md5:	6fd3dc7f0ce9ca20a540372711533472
URL:		http://search.cpan.org/dist/Socket-GetAddrInfo/
BuildRequires:	perl-ExtUtils-CChecker >= 0.06
%{?with_tests:BuildRequires:	perl-Test-Pod}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RFC 2553 functions getaddrinfo and getnameinfo provide an
abstracted way to convert between a pair of host name/service name and
socket addresses, or vice versa. getaddrinfo converts names into a set
of arguments to pass to the socket() and connect() syscalls, and
getnameinfo converts a socket address back into its host name/service
name pair.

%description -l pl.UTF-8
Zgodne z RFC 2553 funkcje getaddrinfo i getnameinfo udostępniają
abstrakcyjne metody do konwersji pary nazw hosta i usługi na adresy
gniazda i z powrotem. getaddrinfo konwertuje nazwy na zbiór argumentów
do przekazania funkcjom socket() i connect(), natomiast getnameinfo
przekształca adres gniazda z powrotem na parę nazw hosta i usługi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/getaddrinfo
%attr(755,root,root) %{_bindir}/getnameinfo
%dir %{perl_vendorarch}/Socket
%{perl_vendorarch}/Socket/GetAddrInfo.pm
%dir %{perl_vendorarch}/Socket/GetAddrInfo
%{perl_vendorarch}/Socket/GetAddrInfo/*.pm
%dir %{perl_vendorarch}/auto/Socket
%dir %{perl_vendorarch}/auto/Socket/GetAddrInfo
%{perl_vendorarch}/auto/Socket/GetAddrInfo/GetAddrInfo.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Socket/GetAddrInfo/GetAddrInfo.so
%{_mandir}/man1/getaddrinfo.1p*
%{_mandir}/man1/getnameinfo.1p*
%{_mandir}/man3/Socket::GetAddrInfo*.3pm*