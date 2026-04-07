import { Form, Head } from '@inertiajs/react';
import InputError from '@/components/input-error';
import LogoES from '@/components/logo-es';
import { update } from '@/routes/password';

type Props = {
    token: string;
    email: string;
};

export default function ResetPassword({ token, email }: Props) {
    const inp = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';

    return (
        <div className="min-h-screen bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] flex items-center justify-center px-4 py-10 relative overflow-hidden">
            <Head title="Reset password" />
            <div className="absolute top-20 left-10 w-72 h-72 bg-yellow-300/10 rounded-full blur-3xl" />
            <div className="absolute bottom-20 right-10 w-96 h-96 bg-blue-300/10 rounded-full blur-3xl" />

            <div className="bg-white dark:bg-gray-800 rounded-3xl shadow-2xl p-8 md:p-10 w-full max-w-md relative">
                <div className="text-center mb-8">
                    <div className="w-14 h-14 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg shadow-blue-200 dark:shadow-blue-900/30">
                        <LogoES className="w-8 h-8" />
                    </div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Reset Password</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Enter your new password below</p>
                </div>

                <Form
                    {...update.form()}
                    transform={(data) => ({ ...data, token, email })}
                    resetOnSuccess={['password', 'password_confirmation']}
                    className="space-y-4"
                >
                    {({ processing, errors }) => (
                        <>
                            <div>
                                <label htmlFor="email" className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Email Address</label>
                                <input
                                    id="email"
                                    type="email"
                                    name="email"
                                    autoComplete="email"
                                    value={email}
                                    readOnly
                                    className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm bg-gray-100 dark:bg-gray-700 text-gray-400 dark:text-gray-500 cursor-not-allowed"
                                />
                                <InputError message={errors.email} />
                            </div>

                            <div>
                                <label htmlFor="password" className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">New Password</label>
                                <input
                                    id="password"
                                    type="password"
                                    name="password"
                                    required
                                    autoFocus
                                    autoComplete="new-password"
                                    placeholder="Enter new password"
                                    className={inp}
                                />
                                <InputError message={errors.password} />
                            </div>

                            <div>
                                <label htmlFor="password_confirmation" className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Confirm Password</label>
                                <input
                                    id="password_confirmation"
                                    type="password"
                                    name="password_confirmation"
                                    required
                                    autoComplete="new-password"
                                    placeholder="Re-enter new password"
                                    className={inp}
                                />
                                <InputError message={errors.password_confirmation} />
                            </div>

                            <button
                                type="submit"
                                disabled={processing}
                                data-test="reset-password-button"
                                className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30 transition-all duration-200 text-sm font-semibold mt-2 disabled:opacity-50"
                            >
                                {processing ? (
                                    <span className="flex items-center justify-center gap-2">
                                        <i className="fa-solid fa-spinner fa-spin" /> Resetting...
                                    </span>
                                ) : 'Reset Password'}
                            </button>
                        </>
                    )}
                </Form>
            </div>
        </div>
    );
}
