import { createInertiaApp } from '@inertiajs/react';
import { TooltipProvider } from '@/components/ui/tooltip';
import { initializeTheme } from '@/hooks/use-appearance';
import AuthLayout from '@/layouts/auth-layout';
import SettingsLayout from '@/layouts/settings/layout';
import StudentLayout from '@/layouts/student-layout';

const appName = import.meta.env.VITE_APP_NAME || 'Eternal Sunshine';

createInertiaApp({
    title: (title) => (title ? `${title} - ${appName}` : appName),
    layout: (name) => {
        switch (true) {
            case name === 'welcome':
            case name === 'auth/login':
            case name === 'auth/register':
            case name === 'auth/forgot-password':
            case name === 'auth/reset-password':
                return null;
            case name.startsWith('auth/'):
                return AuthLayout;
            case name.startsWith('settings/'):
                return [StudentLayout, SettingsLayout];
            default:
                return undefined;
        }
    },
    strictMode: true,
    withApp(app) {
        return <TooltipProvider delayDuration={0}>{app}</TooltipProvider>;
    },
    progress: {
        color: '#2563EB',
    },
});

// This will set light / dark mode on load...
initializeTheme();
