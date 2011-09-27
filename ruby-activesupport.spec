%define	rname	activesupport

Summary:	Support and utility classes used by the Rails framework
Name:		ruby-%{rname}
Version:	3.1.0
Release:	%mkrel 1
URL:		http://as.rubyonrails.com/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
BuildRequires:	ruby-rdoc 
Provides:	rubygem(%{rname})

%description
Utility library which carries commonly used classes and goodies from the Rails
framework.

%prep

%build

%install
rm -rf %{buildroot}
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
