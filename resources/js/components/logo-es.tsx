export default function LogoES({ className = 'w-6 h-6' }: { className?: string }) {
  return (
    <svg className={className} viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g stroke="#FBBF24" strokeWidth="2" strokeLinecap="round">
        <line x1="20" y1="2" x2="20" y2="7" />
        <line x1="20" y1="33" x2="20" y2="38" />
        <line x1="7.27" y1="7.27" x2="10.81" y2="10.81" />
        <line x1="29.19" y1="29.19" x2="32.73" y2="32.73" />
        <line x1="2" y1="20" x2="7" y2="20" />
        <line x1="33" y1="20" x2="38" y2="20" />
        <line x1="7.27" y1="32.73" x2="10.81" y2="29.19" />
        <line x1="29.19" y1="10.81" x2="32.73" y2="7.27" />
      </g>
      <circle cx="20" cy="20" r="11" fill="url(#sunGrad)" />
      <path d="M14 17.5C14 17.5 17 16.5 20 18C23 16.5 26 17.5 26 17.5V24.5C26 24.5 23 23.5 20 25C17 23.5 14 24.5 14 24.5V17.5Z" fill="white" fillOpacity="0.95" />
      <line x1="20" y1="18" x2="20" y2="25" stroke="#FBBF24" strokeWidth="0.8" />
      <defs>
        <linearGradient id="sunGrad" x1="9" y1="9" x2="31" y2="31">
          <stop stopColor="#F59E0B" />
          <stop offset="1" stopColor="#EF6C00" />
        </linearGradient>
      </defs>
    </svg>
  );
}
