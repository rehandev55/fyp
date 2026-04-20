import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\AIControllers\AIController::chat
 * @see app/Http/Controllers/AIControllers/AIController.php:15
 * @route '/api/chat'
 */
export const chat = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: chat.url(options),
    method: 'post',
})

chat.definition = {
    methods: ["post"],
    url: '/api/chat',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\AIController::chat
 * @see app/Http/Controllers/AIControllers/AIController.php:15
 * @route '/api/chat'
 */
chat.url = (options?: RouteQueryOptions) => {
    return chat.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\AIController::chat
 * @see app/Http/Controllers/AIControllers/AIController.php:15
 * @route '/api/chat'
 */
chat.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: chat.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\AIController::chat
 * @see app/Http/Controllers/AIControllers/AIController.php:15
 * @route '/api/chat'
 */
    const chatForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: chat.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\AIController::chat
 * @see app/Http/Controllers/AIControllers/AIController.php:15
 * @route '/api/chat'
 */
        chatForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: chat.url(options),
            method: 'post',
        })
    
    chat.form = chatForm
/**
* @see \App\Http\Controllers\AIControllers\AIController::generateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:21
 * @route '/api/quiz/generate'
 */
export const generateQuiz = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: generateQuiz.url(options),
    method: 'post',
})

generateQuiz.definition = {
    methods: ["post"],
    url: '/api/quiz/generate',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\AIController::generateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:21
 * @route '/api/quiz/generate'
 */
generateQuiz.url = (options?: RouteQueryOptions) => {
    return generateQuiz.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\AIController::generateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:21
 * @route '/api/quiz/generate'
 */
generateQuiz.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: generateQuiz.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\AIController::generateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:21
 * @route '/api/quiz/generate'
 */
    const generateQuizForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: generateQuiz.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\AIController::generateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:21
 * @route '/api/quiz/generate'
 */
        generateQuizForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: generateQuiz.url(options),
            method: 'post',
        })
    
    generateQuiz.form = generateQuizForm
/**
* @see \App\Http\Controllers\AIControllers\AIController::evaluateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:27
 * @route '/api/quiz/evaluate'
 */
export const evaluateQuiz = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: evaluateQuiz.url(options),
    method: 'post',
})

evaluateQuiz.definition = {
    methods: ["post"],
    url: '/api/quiz/evaluate',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\AIController::evaluateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:27
 * @route '/api/quiz/evaluate'
 */
evaluateQuiz.url = (options?: RouteQueryOptions) => {
    return evaluateQuiz.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\AIController::evaluateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:27
 * @route '/api/quiz/evaluate'
 */
evaluateQuiz.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: evaluateQuiz.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\AIController::evaluateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:27
 * @route '/api/quiz/evaluate'
 */
    const evaluateQuizForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: evaluateQuiz.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\AIController::evaluateQuiz
 * @see app/Http/Controllers/AIControllers/AIController.php:27
 * @route '/api/quiz/evaluate'
 */
        evaluateQuizForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: evaluateQuiz.url(options),
            method: 'post',
        })
    
    evaluateQuiz.form = evaluateQuizForm
const AIController = { chat, generateQuiz, evaluateQuiz }

export default AIController