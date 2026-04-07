import { Form, Head, Link } from '@inertiajs/react';
import InputError from '@/components/input-error';
import LogoES from '@/components/logo-es';
import { store } from '@/routes/login';
import { register } from '@/routes';
import { request } from '@/routes/password';

type Props = {
    status?: string;
    canResetPassword: boolean;
    canRegister: boolean;
};

export default function Login({ status, canResetPassword, canRegister }: Props) {
    return (
        <div className="min-h-screen bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] flex items-center justify-center px-4 relative overflow-hidden">
            <Head title="Log in" />
            <div className="absolute top-20 left-10 w-72 h-72 bg-yellow-300/10 rounded-full blur-3xl" />
            <div className="absolute bottom-20 right-10 w-96 h-96 bg-blue-300/10 rounded-full blur-3xl" />

            <div className="bg-white dark:bg-gray-800 rounded-3xl shadow-2xl p-8 md:p-10 w-full max-w-md relative">
                <div className="text-center mb-8">
                    <div className="w-14 h-14 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg shadow-blue-200 dark:shadow-blue-900/30">
                        <LogoES className="w-8 h-8" />
                    </div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Welcome Back</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Sign in to your account</p>
                </div>

                {status && (
                    <div className="bg-emerald-50 dark:bg-emerald-900/30 border border-emerald-200 dark:border-emerald-800 text-emerald-600 dark:text-emerald-400 text-sm px-4 py-3 rounded-xl mb-5 flex items-center gap-2">
                        <i className="fa-solid fa-circle-check" />
                        {status}
                    </div>
                )}

                <Form
                    {...store.form()}
                    resetOnSuccess={['password']}
                    className="space-y-5"
                >
                    {({ processing, errors }) => (
                        <>
                            <div>
                                <label htmlFor="email" className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Email Address</label>
                                <input
                                    id="email"
                                    type="email"
                                    name="email"
                                    required
                                    autoFocus
                                    autoComplete="email"
                                    placeholder="you@example.com"
                                    className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition"
                                />
                                <InputError message={errors.email} />
                            </div>

                            <div>
                                <div className="flex items-center justify-between mb-2">
                                    <label htmlFor="password" className="block text-sm font-semibold text-gray-700 dark:text-gray-200">Password</label>
                                    {canResetPassword && (
                                        <Link href={request()} className="text-xs text-[#2563EB] hover:underline font-medium">
                                            Forgot password?
                                        </Link>
                                    )}
                                </div>
                                <input
                                    id="password"
                                    type="password"
                                    name="password"
                                    required
                                    autoComplete="current-password"
                                    placeholder="Enter your password"
                                    className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition"
                                />
                                <InputError message={errors.password} />
                            </div>

                            <div className="flex items-center gap-2">
                                <input type="checkbox" id="remember" name="remember" className="w-4 h-4 rounded border-gray-300 text-[#2563EB] focus:ring-[#2563EB]" />
                                <label htmlFor="remember" className="text-sm text-gray-600 dark:text-gray-300">Remember me</label>
                            </div>

                            <button
                                type="submit"
                                disabled={processing}
                                className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30 transition-all duration-200 text-sm font-semibold disabled:opacity-50"
                            >
                                {processing ? (
                                    <span className="flex items-center justify-center gap-2">
                                        <i className="fa-solid fa-spinner fa-spin" /> Signing in...
                                    </span>
                                ) : 'Sign In'}
                            </button>

                            {canRegister && (
                                <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-2">
                                    Don&apos;t have an account?{' '}
                                    <Link href={register()} className="text-[#2563EB] hover:underline font-semibold">Create Account</Link>
                                </p>
                            )}
                        </>
                    )}
                </Form>
            </div>
        </div>
    );
}
