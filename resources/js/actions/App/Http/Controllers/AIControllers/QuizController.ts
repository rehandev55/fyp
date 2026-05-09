import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\AIControllers\QuizController::evaluate
 * @see app/Http/Controllers/AIControllers/QuizController.php:16
 * @route '/api/quiz/evaluate'
 */
export const evaluate = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: evaluate.url(options),
    method: 'post',
})

evaluate.definition = {
    methods: ["post"],
    url: '/api/quiz/evaluate',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\QuizController::evaluate
 * @see app/Http/Controllers/AIControllers/QuizController.php:16
 * @route '/api/quiz/evaluate'
 */
evaluate.url = (options?: RouteQueryOptions) => {
    return evaluate.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\QuizController::evaluate
 * @see app/Http/Controllers/AIControllers/QuizController.php:16
 * @route '/api/quiz/evaluate'
 */
evaluate.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: evaluate.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\QuizController::evaluate
 * @see app/Http/Controllers/AIControllers/QuizController.php:16
 * @route '/api/quiz/evaluate'
 */
    const evaluateForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: evaluate.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\QuizController::evaluate
 * @see app/Http/Controllers/AIControllers/QuizController.php:16
 * @route '/api/quiz/evaluate'
 */
        evaluateForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: evaluate.url(options),
            method: 'post',
        })
    
    evaluate.form = evaluateForm
/**
* @see \App\Http\Controllers\AIControllers\QuizController::overall
 * @see app/Http/Controllers/AIControllers/QuizController.php:29
 * @route '/api/quiz/overall'
 */
export const overall = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: overall.url(options),
    method: 'post',
})

overall.definition = {
    methods: ["post"],
    url: '/api/quiz/overall',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\QuizController::overall
 * @see app/Http/Controllers/AIControllers/QuizController.php:29
 * @route '/api/quiz/overall'
 */
overall.url = (options?: RouteQueryOptions) => {
    return overall.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\QuizController::overall
 * @see app/Http/Controllers/AIControllers/QuizController.php:29
 * @route '/api/quiz/overall'
 */
overall.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: overall.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\QuizController::overall
 * @see app/Http/Controllers/AIControllers/QuizController.php:29
 * @route '/api/quiz/overall'
 */
    const overallForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: overall.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\QuizController::overall
 * @see app/Http/Controllers/AIControllers/QuizController.php:29
 * @route '/api/quiz/overall'
 */
        overallForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: overall.url(options),
            method: 'post',
        })
    
    overall.form = overallForm
const QuizController = { evaluate, overall }

export default QuizController