%define	rname	activesupport

Summary:	Support and utility classes used by the Rails framework
Name:		ruby-%{rname}
Version:	3.2.3
Release:	1
URL:		http://as.rubyonrails.com/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
Provides:	rubygem(%{rname})

%description
Utility library which carries commonly used classes and goodies from the Rails
framework.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --no-rdoc --no-ri --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
