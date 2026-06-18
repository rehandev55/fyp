export const API_URL = import.meta.env.VITE_API_URL;

export async function backendApi(
    path: string,
    options: RequestInit = {}
): Promise<Response> {
    return fetch(`${API_URL}${path}`, {
        credentials: 'include',
        headers: {
            Accept: 'application/json',
            ...(options.headers || {}),
        },
        ...options,
    });
}
