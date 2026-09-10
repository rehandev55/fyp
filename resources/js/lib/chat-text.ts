/** Splits text into alternating plain / code segments so code is never rewritten. */
const CODE_SEGMENTS = /(```[\s\S]*?```|`[^`\n]*`)/g;

/**
 * The AI service emits LaTeX with `\( ... \)` and `\[ ... \]` delimiters, which
 * remark-math does not understand. Rewrite them to the `$` / `$$` form it does.
 */
export function normalizeMath(text: string): string {
    return text
        .split(CODE_SEGMENTS)
        .map((segment, index) => {
            if (index % 2 === 1) {
                return segment;
            }

            return segment
                .replace(/\\\[([\s\S]*?)\\\]/g, (_, body: string) => `\n\n$$${body.trim()}$$\n\n`)
                .replace(/\\\(([\s\S]*?)\\\)/g, (_, body: string) => `$${body.trim()}$`);
        })
        .join('');
}

const SPEECH_REPLACEMENTS: Array<[RegExp, string]> = [
    [/\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, ' $1 over $2 '],
    [/\\sqrt\s*\[\s*2\s*\]\s*\{([^{}]*)\}/g, ' square root of $1 '],
    [/\\sqrt\s*\[\s*3\s*\]\s*\{([^{}]*)\}/g, ' cube root of $1 '],
    [/\\sqrt\s*\[([^\]]*)\]\s*\{([^{}]*)\}/g, ' $1th root of $2 '],
    [/\\sqrt\s*\{([^{}]*)\}/g, ' square root of $1 '],
    [/\\times/g, ' times '],
    [/\\div/g, ' divided by '],
    [/\\pm/g, ' plus or minus '],
    [/\\leq/g, ' less than or equal to '],
    [/\\geq/g, ' greater than or equal to '],
    [/\\neq/g, ' not equal to '],
    [/\\ldots|\\dots|\\cdots/g, ' and so on '],
    [/\\(?:text|mathrm|mathbf|textbf|mathit)\s*\{([^{}]*)\}/g, '$1'],
    [/\^\s*\{?([^{}\s]+)\}?/g, ' to the power $1 '],
    [/_\s*\{?([^{}\s]+)\}?/g, ' $1 '],
];

/**
 * Flattens markdown and LaTeX into something a speech synthesiser can read aloud
 * without spelling out backslashes, asterisks and braces.
 */
export function stripForSpeech(text: string): string {
    let speech = text
        .replace(/```[\s\S]*?```/g, ' code block ')
        .replace(/\$\$([\s\S]*?)\$\$/g, ' $1 ')
        .replace(/\\\[([\s\S]*?)\\\]/g, ' $1 ')
        .replace(/\\\(([\s\S]*?)\\\)/g, ' $1 ')
        .replace(/\$([^$\n]*)\$/g, ' $1 ');

    for (const [pattern, replacement] of SPEECH_REPLACEMENTS) {
        speech = speech.replace(pattern, replacement);
    }

    return speech
        .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
        .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
        .replace(/^\s{0,3}#{1,6}\s*/gm, '')
        .replace(/^\s{0,3}>\s?/gm, '')
        .replace(/^\s*[-*+]\s+/gm, '')
        .replace(/[*_~`{}\\]/g, '')
        .replace(/[ \t]{2,}/g, ' ')
        .replace(/\n{3,}/g, '\n\n')
        .trim();
}
