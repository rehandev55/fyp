function getCookie(name: string): string | null {
    const match = document.cookie.match(new RegExp('(^|;\\s*)' + name + '=([^;]*)'));
    return match ? decodeURIComponent(match[2]) : null;
}

async function ensureCsrf(): Promise<void> {
    if (!getCookie('XSRF-TOKEN')) {
        await fetch('/sanctum/csrf-cookie', { credentials: 'include' });
    }
}

export async function api(path: string, options: RequestInit = {}): Promise<Response> {
    await ensureCsrf();

    const headers: Record<string, string> = {
        Accept: 'application/json',
        ...(options.headers as Record<string, string>),
    };

    const xsrf = getCookie('XSRF-TOKEN');
    if (xsrf) {
        headers['X-XSRF-TOKEN'] = xsrf;
    }

    // Don't set Content-Type for FormData (browser sets it with boundary)
    if (!(options.body instanceof FormData) && !headers['Content-Type']) {
        headers['Content-Type'] = 'application/json';
    }

    return fetch(`/api${path}`, {
        credentials: 'include',
        ...options,
        headers,
    });
}
