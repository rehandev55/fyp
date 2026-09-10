import { memo } from 'react';
import Markdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import { normalizeMath } from '@/lib/chat-text';
import 'katex/dist/katex.min.css';

const KATEX_OPTIONS = {
    throwOnError: false,
    strict: false,
    trust: false,
    errorColor: '#dc2626',
};

/**
 * Renders an assistant reply as markdown with typeset LaTeX maths.
 */
function ChatMarkdown({ text }: { text: string }) {
    return (
        <div className="chat-markdown text-sm leading-relaxed break-words">
            <Markdown
                remarkPlugins={[remarkGfm, remarkMath]}
                rehypePlugins={[[rehypeKatex, KATEX_OPTIONS]]}
                components={{
                    h1: ({ children }) => <h1 className="mt-4 mb-2 text-base font-bold first:mt-0">{children}</h1>,
                    h2: ({ children }) => <h2 className="mt-4 mb-2 text-base font-bold first:mt-0">{children}</h2>,
                    h3: ({ children }) => <h3 className="mt-4 mb-1.5 text-sm font-bold first:mt-0">{children}</h3>,
                    h4: ({ children }) => <h4 className="mt-3 mb-1.5 text-sm font-semibold first:mt-0">{children}</h4>,
                    p: ({ children }) => <p className="my-2 first:mt-0 last:mb-0">{children}</p>,
                    strong: ({ children }) => <strong className="font-semibold text-gray-900 dark:text-white">{children}</strong>,
                    em: ({ children }) => <em className="italic">{children}</em>,
                    ul: ({ children }) => <ul className="my-2 list-disc space-y-1 pl-5">{children}</ul>,
                    ol: ({ children }) => <ol className="my-2 list-decimal space-y-1 pl-5">{children}</ol>,
                    li: ({ children }) => <li className="marker:text-gray-400">{children}</li>,
                    a: ({ children, href }) => (
                        <a href={href} target="_blank" rel="noopener noreferrer" className="text-[#2563EB] underline underline-offset-2 hover:opacity-80">
                            {children}
                        </a>
                    ),
                    blockquote: ({ children }) => (
                        <blockquote className="my-2 border-l-2 border-[#2563EB] pl-3 text-gray-600 italic dark:text-gray-300">{children}</blockquote>
                    ),
                    hr: () => <hr className="my-3 border-gray-200 dark:border-gray-700" />,
                    code: ({ children }) => (
                        <code className="rounded bg-gray-100 px-1 py-0.5 font-mono text-[0.85em] text-[#7C3AED] dark:bg-gray-700 dark:text-purple-300">
                            {children}
                        </code>
                    ),
                    pre: ({ children }) => (
                        <pre className="my-2 overflow-x-auto rounded-xl bg-gray-900 p-3 font-mono text-xs text-gray-100 [&_code]:bg-transparent [&_code]:p-0 [&_code]:text-inherit">
                            {children}
                        </pre>
                    ),
                    table: ({ children }) => (
                        <div className="my-2 overflow-x-auto">
                            <table className="w-full border-collapse text-xs">{children}</table>
                        </div>
                    ),
                    th: ({ children }) => (
                        <th className="border border-gray-200 bg-gray-50 px-2 py-1 text-left font-semibold dark:border-gray-700 dark:bg-gray-700/50">
                            {children}
                        </th>
                    ),
                    td: ({ children }) => <td className="border border-gray-200 px-2 py-1 dark:border-gray-700">{children}</td>,
                }}
            >
                {normalizeMath(text)}
            </Markdown>
        </div>
    );
}

export default memo(ChatMarkdown);
