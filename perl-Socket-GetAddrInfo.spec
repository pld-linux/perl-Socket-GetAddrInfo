#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Socket
%define	pnam	GetAddrInfo
Summary:	Socket::GetAddrInfo - RFC 2553's getaddrinfo and getnameinfo functions
#Summary(pl.UTF-8):
Name:		perl-Socket-GetAddrInfo
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Socket-GetAddrInfo-%{version}.tar.gz
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

These functions provide a useful interface for performing either of
these name resolution operation, without having to deal with IPv4/IPv6
transparency, or whether the underlying host can support IPv6 at all,
or other such issues. However, not all platforms can support the
underlying calls at the C layer, which means a dilema for authors
wishing to write forward-compatible code. Either to support these
functions, and cause the code not to work on older platforms, or stick
to the older "legacy" resolvers such as gethostbyname(), which means
the code becomes more portable.

This module attempts to solve this problem, by detecting at
compiletime whether the underlying OS will support these functions,
and only compiling the XS code if it can. At runtime, when the module
is loaded, if the XS implementation is not available, emulations of
the functions using the legacy resolver functions instead. The
emulations support the same interface as the real functions, and
behave as close as is resonably possible to emulate using the legacy
resolvers. See below for details on the limits of this emulation.

# %description -l pl.UTF-8
# TODO

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
%dir %{perl_vendorarch}/Socket
%{perl_vendorarch}/Socket/*.pm
%dir %{perl_vendorarch}/auto/Socket
%dir %{perl_vendorarch}/auto/Socket/GetAddrInfo
%{perl_vendorarch}/auto/Socket/GetAddrInfo/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Socket/GetAddrInfo/*.so
%dir %{perl_vendorarch}/Socket/GetAddrInfo
%{perl_vendorarch}/Socket/GetAddrInfo/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/get*info.*
%attr(755,root,root) %{_bindir}/getaddrinfo
%attr(755,root,root) %{_bindir}/getnameinfo
